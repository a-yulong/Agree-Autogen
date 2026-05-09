package org.agreeautogen.validator;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.URISyntaxException;
import java.nio.charset.StandardCharsets;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.Set;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.stream.Collectors;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.plugin.EcorePlugin;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.xtext.diagnostics.Severity;
import org.eclipse.xtext.resource.XtextResource;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.eclipse.xtext.util.CancelIndicator;
import org.eclipse.xtext.validation.CheckMode;
import org.eclipse.xtext.validation.IResourceValidator;
import org.eclipse.xtext.validation.Issue;
import org.osate.annexsupport.AnnexRegistry;
import org.osate.xtext.aadl2.Aadl2StandaloneSetup;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import com.google.inject.Injector;
import com.rockwellcollins.atc.agree.AgreeStandaloneSetup;

public final class AgreeValidationCli {
    private AgreeValidationCli() {
    }

    public static void main(String[] args) throws Exception {
        Args parsed = Args.parse(args);
        if (parsed.help) {
            printUsage();
            return;
        }

        List<String> missing = new ArrayList<>();
        if (parsed.workspace == null) {
            missing.add("--workspace");
        }
        if (parsed.project == null) {
            missing.add("--project");
        }
        if (parsed.osateHome == null) {
            missing.add("--osate-home");
        }
        if (!missing.isEmpty()) {
            throw new IllegalArgumentException("Missing required arguments: " + String.join(", ", missing));
        }

        Path workspace = parsed.workspace.toAbsolutePath().normalize();
        Path projectPath = parsed.project.isAbsolute()
                ? parsed.project.toAbsolutePath().normalize()
                : workspace.resolve(parsed.project).toAbsolutePath().normalize();
        Path osateHome = parsed.osateHome.toAbsolutePath().normalize();
        PrintStream originalOut = System.out;
        PrintStream originalErr = System.err;
        ValidationReport report;
        try {
            silenceRuntimeLogging();
            Injector injector = new Aadl2StandaloneSetup().createInjectorAndDoEMFRegistration();
            Injector agreeInjector = new AgreeStandaloneSetup().createInjectorAndDoEMFRegistration();
            registerAgreeAnnexSupport(agreeInjector);
            XtextResourceSet resourceSet = injector.getInstance(XtextResourceSet.class);
            if (resourceSet == null) {
                throw new IllegalStateException("Unable to create XtextResourceSet");
            }

            List<Path> expandedLibs = expandLibDirs(parsed.libs, parsed.libDirs);
            Path bundledStaticLibDir = findBundledStaticLibDir();
            if (bundledStaticLibDir != null) {
                expandedLibs = expandLibDirs(expandedLibs, List.of(bundledStaticLibDir));
            }
            LoadResult loadResult = loadProjectAadlFiles(workspace, projectPath, expandedLibs, resourceSet);
            loadContributedResources(osateHome, loadResult.loadedFileNames, resourceSet);
            EcoreUtil.resolveAll(resourceSet);
            report = validateResourceSet(resourceSet, parsed.focusFile);
        } finally {
            System.setOut(originalOut);
            System.setErr(originalErr);
        }

        String json = report.toJson();
        if (parsed.output != null) {
            Path output = parsed.output.toAbsolutePath().normalize();
            if (output.getParent() != null) {
                Files.createDirectories(output.getParent());
            }
            Files.writeString(output, json, StandardCharsets.UTF_8);
        }

        System.out.println(json);
        if (report.errors > 0 || (parsed.failOnWarning && report.warnings > 0)) {
            System.exit(2);
        }
    }

    private static void printUsage() {
        System.out.println(String.join(System.lineSeparator(),
                "Usage:",
                "  java ... org.agreeautogen.validator.AgreeValidationCli \\",
                "      --workspace <workspaceDir> \\",
                "      --project <projectDir|relativeProjectPath> \\",
                "      --osate-home <osateInstallDir> \\",
                "      [--output <jsonFile>] \\",
                "      [--focus-file <aadlFileName>] \\",
                "      [--lib <aadlFile>]... \\",
                "      [--lib-dir <aadlDirectory>]... \\",
                "      [--fail-on-warning]",
                "",
                "Notes:",
                "  --project can be an absolute path or a path relative to --workspace.",
                "  --focus-file limits reported issues to a specific platform resource file name.",
                "  static-libs under the validator root are loaded automatically when present.",
                "  --lib can be repeated to add extra AADL libraries outside the workspace.",
                "  --lib-dir can be repeated to recursively add all .aadl files under a directory.",
                "  OSATE built-in AADL resources are loaded automatically unless a same-named file",
                "  already exists in the workspace project or referenced libraries."));
    }

    private static void registerAgreeAnnexSupport(Injector agreeInjector) {
        AnnexRegistry.registerParser("agree", new StandaloneAgreeAnnexParser(agreeInjector));
        AnnexRegistry.registerLinkingService("agree", new StandaloneAgreeAnnexLinkingService(agreeInjector));
    }

    private static void silenceRuntimeLogging() {
        PrintStream nullStream = new PrintStream(OutputStream.nullOutputStream(), true, StandardCharsets.UTF_8);
        System.setOut(nullStream);
        System.setErr(nullStream);
    }

    private static Path findBundledStaticLibDir() {
        try {
            Path codeSource = Paths.get(AgreeValidationCli.class.getProtectionDomain()
                    .getCodeSource()
                    .getLocation()
                    .toURI());
            Path current = Files.isDirectory(codeSource) ? codeSource : codeSource.getParent();
            while (current != null) {
                Path candidate = current.resolve("static-libs");
                if (Files.isDirectory(candidate)) {
                    return candidate;
                }
                current = current.getParent();
            }
        } catch (URISyntaxException ex) {
            return null;
        }
        return null;
    }

    private static void loadContributedResources(Path osateHome, Set<String> skipFileNames, ResourceSet resourceSet)
            throws Exception {
        Path pluginsDir = osateHome.resolve("plugins");
        if (!Files.isDirectory(pluginsDir)) {
            throw new IllegalArgumentException("OSATE plugins directory not found: " + pluginsDir);
        }

        List<Path> pluginArtifacts = Files.list(pluginsDir)
                .filter(path -> path.getFileName().toString().endsWith(".jar") || Files.isDirectory(path))
                .sorted()
                .collect(Collectors.toList());

        for (Path artifact : pluginArtifacts) {
            if (Files.isDirectory(artifact)) {
                loadContributedResourcesFromDirectory(artifact, skipFileNames, resourceSet);
            } else {
                loadContributedResourcesFromJar(artifact, skipFileNames, resourceSet);
            }
        }
    }

    private static void loadContributedResourcesFromDirectory(Path pluginDir, Set<String> skipFileNames,
            ResourceSet resourceSet) throws Exception {
        Path resourcesDir = pluginDir.resolve("resources");
        if (!Files.isDirectory(resourcesDir)) {
            return;
        }

        Files.walkFileTree(resourcesDir, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                if (file.getFileName().toString().toLowerCase().endsWith(".aadl")
                        && !skipFileNames.contains(file.getFileName().toString().toLowerCase())) {
                    String relative = resourcesDir.relativize(file).toString().replace("\\", "/");
                    String pluginName = pluginDir.getFileName().toString();
                    URI uri = URI.createPlatformResourceURI("Plugin_Resources/" + pluginName + "/" + relative, true);
                    try (InputStream stream = Files.newInputStream(file)) {
                        loadResource(resourceSet, uri, stream);
                    }
                }
                return FileVisitResult.CONTINUE;
            }
        });
    }

    private static void loadContributedResourcesFromJar(Path jarPath, Set<String> skipFileNames, ResourceSet resourceSet)
            throws Exception {
        try (JarFile jarFile = new JarFile(jarPath.toFile())) {
            List<JarEntry> entries = jarFile.stream()
                    .filter(entry -> !entry.isDirectory())
                    .filter(entry -> isContributedAadl(entry.getName()))
                    .filter(entry -> !skipFileNames.contains(Paths.get(entry.getName()).getFileName().toString().toLowerCase()))
                    .sorted(Comparator.comparing(JarEntry::getName))
                    .collect(Collectors.toList());

            String pluginName = jarPath.getFileName().toString().replace(".jar", "");
            for (JarEntry entry : entries) {
                String relative = entry.getName().substring("resources/".length());
                URI uri = URI.createPlatformResourceURI("Plugin_Resources/" + pluginName + "/" + relative, true);
                try (InputStream stream = jarFile.getInputStream(entry)) {
                    loadResource(resourceSet, uri, stream);
                }
            }
        }
    }

    private static boolean isContributedAadl(String entryName) {
        if (!entryName.startsWith("resources/")) {
            return false;
        }
        if (!entryName.toLowerCase().endsWith(".aadl")) {
            return false;
        }
        return !entryName.contains("/examples/");
    }

    private static Resource loadResource(ResourceSet resourceSet, URI uri, InputStream stream) throws IOException {
        Resource existing = resourceSet.getResource(uri, false);
        if (existing != null) {
            return existing;
        }

        Resource resource = resourceSet.createResource(uri);
        if (resource == null) {
            throw new IOException("Unable to create resource for " + uri);
        }
        resource.load(stream, Collections.emptyMap());
        return resource;
    }

    private static LoadResult loadProjectAadlFiles(Path workspace, Path projectPath, List<Path> extraLibs,
            XtextResourceSet resourceSet) throws Exception {
        if (!Files.isDirectory(projectPath)) {
            throw new IllegalArgumentException("Project directory not found: " + projectPath);
        }

        String projectName = getProjectName(projectPath.resolve(".project"));
        EcorePlugin.getPlatformResourceMap().put(projectName, URI.createFileURI(projectPath.toString()));
        Set<String> loadedFileNames = new HashSet<>();

        List<Path> projectAadlFiles = findAadlFiles(projectPath);
        for (Path aadlFile : projectAadlFiles) {
            loadedFileNames.add(aadlFile.getFileName().toString().toLowerCase());
        }
        for (Path lib : extraLibs) {
            loadedFileNames.add(lib.getFileName().toString().toLowerCase());
        }

        Map<String, List<Path>> projectMap = findProjects(workspace);
        List<Path> sameNameProjects = projectMap.getOrDefault(projectName, new ArrayList<>());
        ListIterator<Path> iterator = sameNameProjects.listIterator();
        while (iterator.hasNext()) {
            Path path = iterator.next();
            if (!path.equals(projectPath)) {
                iterator.remove();
            }
        }

        List<Path> referencedProjects = new ArrayList<>();
        getReferenceProjectPaths(referencedProjects, projectName, projectMap);
        for (Path refProject : referencedProjects) {
            for (Path aadlFile : findAadlFiles(refProject)) {
                loadedFileNames.add(aadlFile.getFileName().toString().toLowerCase());
            }
        }

        for (Path aadlFile : projectAadlFiles) {
            loadWorkspaceFile(projectPath, projectName, aadlFile, resourceSet);
        }

        for (Path lib : extraLibs) {
            loadExternalLib(lib, resourceSet);
        }
        for (Path refProject : referencedProjects) {
            String refProjectName = getProjectName(refProject.resolve(".project"));
            EcorePlugin.getPlatformResourceMap().put(refProjectName, URI.createFileURI(refProject.toString()));
            for (Path aadlFile : findAadlFiles(refProject)) {
                loadWorkspaceFile(refProject, refProjectName, aadlFile, resourceSet);
            }
        }

        EcoreUtil.resolveAll(resourceSet);
        return new LoadResult(projectName, loadedFileNames);
    }

    private static List<Path> findAadlFiles(Path root) throws IOException {
        List<Path> result = new ArrayList<>();
        Files.walkFileTree(root, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                if (file.getFileName().toString().toLowerCase().endsWith(".aadl")) {
                    result.add(file);
                }
                return FileVisitResult.CONTINUE;
            }
        });
        result.sort(Comparator.naturalOrder());
        return result;
    }

    private static Map<String, List<Path>> findProjects(Path workspace) throws Exception {
        if (!Files.isDirectory(workspace)) {
            throw new IllegalArgumentException("Workspace directory not found: " + workspace);
        }

        Map<String, List<Path>> projectMap = new HashMap<>();
        Files.walkFileTree(workspace, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                if (file.getFileName().toString().equals(".project")) {
                    try {
                        String projectName = getProjectName(file);
                        projectMap.computeIfAbsent(projectName, key -> new ArrayList<>()).add(file.getParent());
                    } catch (Exception ex) {
                        throw new IOException("Failed to parse " + file, ex);
                    }
                }
                return FileVisitResult.CONTINUE;
            }
        });
        return projectMap;
    }

    private static void getReferenceProjectPaths(List<Path> referencedProjects, String projectName,
            Map<String, List<Path>> projectMap) throws Exception {
        if ("Plugin_Resources".equals(projectName)) {
            return;
        }

        List<Path> projectPaths = projectMap.get(projectName);
        if (projectPaths == null || projectPaths.isEmpty()) {
            throw new IllegalArgumentException("Project not found in workspace: " + projectName);
        }
        if (projectPaths.size() != 1) {
            throw new IllegalArgumentException("Multiple projects found in workspace with same name: " + projectName);
        }

        Path projectPath = projectPaths.get(0);
        for (String refProjectName : getReferenceProjectNames(projectPath.resolve(".project"))) {
            if ("Plugin_Resources".equals(refProjectName)) {
                continue;
            }

            List<Path> refPaths = projectMap.get(refProjectName);
            if (refPaths == null || refPaths.isEmpty()) {
                throw new IllegalArgumentException("Referenced project not found in workspace: " + refProjectName);
            }
            if (refPaths.size() != 1) {
                throw new IllegalArgumentException(
                        "Multiple projects found in workspace with same name: " + refProjectName);
            }

            Path refProjectPath = refPaths.get(0);
            if (!referencedProjects.contains(refProjectPath)) {
                referencedProjects.add(refProjectPath);
                getReferenceProjectPaths(referencedProjects, refProjectName, projectMap);
            }
        }
    }

    private static Resource loadWorkspaceFile(Path projectRoot, String projectName, Path file, ResourceSet resourceSet)
            throws Exception {
        String relative = projectRoot.relativize(file).toString().replace("\\", "/");
        URI resourceUri = URI.createPlatformResourceURI(projectName + "/" + relative, true);
        try (InputStream stream = Files.newInputStream(file)) {
            return loadResource(resourceSet, resourceUri, stream);
        }
    }

    private static Resource loadExternalLib(Path file, ResourceSet resourceSet) throws Exception {
        Path normalized = file.toAbsolutePath().normalize();
        URI resourceUri = URI.createPlatformResourceURI("External_Libs/" + normalized.getFileName(), true);
        try (InputStream stream = Files.newInputStream(normalized)) {
            return loadResource(resourceSet, resourceUri, stream);
        }
    }

    private static List<Path> expandLibDirs(List<Path> libs, List<Path> libDirs) throws IOException {
        List<Path> result = new ArrayList<>();
        Set<Path> seen = new HashSet<>();
        for (Path lib : libs) {
            Path normalized = lib.toAbsolutePath().normalize();
            if (seen.add(normalized)) {
                result.add(normalized);
            }
        }
        for (Path libDir : libDirs) {
            Path normalizedDir = libDir.toAbsolutePath().normalize();
            if (!Files.isDirectory(normalizedDir)) {
                throw new IllegalArgumentException("Library directory not found: " + normalizedDir);
            }
            for (Path aadlFile : findAadlFiles(normalizedDir)) {
                Path normalizedFile = aadlFile.toAbsolutePath().normalize();
                if (seen.add(normalizedFile)) {
                    result.add(normalizedFile);
                }
            }
        }
        return result;
    }

    private static String getProjectName(Path projectFile) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document document = builder.parse(projectFile.toFile());
        document.getDocumentElement().normalize();
        org.w3c.dom.Element root = document.getDocumentElement();
        NodeList list = document.getElementsByTagName("name");
        for (int i = 0; i < list.getLength(); i++) {
            Node node = list.item(i);
            if (node.getNodeType() == Node.ELEMENT_NODE) {
                org.w3c.dom.Element element = (org.w3c.dom.Element) node;
                if (element.getParentNode().isEqualNode(root)) {
                    return element.getTextContent();
                }
            }
        }
        throw new IllegalArgumentException("Unable to read project name from " + projectFile);
    }

    private static List<String> getReferenceProjectNames(Path projectFile) throws Exception {
        List<String> projectNames = new ArrayList<>();
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document document = builder.parse(projectFile.toFile());
        document.getDocumentElement().normalize();
        NodeList list = document.getElementsByTagName("projects");
        for (int i = 0; i < list.getLength(); i++) {
            Node node = list.item(i);
            if (node.getNodeType() == Node.ELEMENT_NODE) {
                org.w3c.dom.Element element = (org.w3c.dom.Element) node;
                NodeList projectNodes = element.getElementsByTagName("project");
                for (int j = 0; j < projectNodes.getLength(); j++) {
                    Node projectNode = projectNodes.item(j);
                    if (projectNode != null) {
                        String text = projectNode.getTextContent();
                        if (text != null && !text.isBlank()) {
                            projectNames.add(text.trim());
                        }
                    }
                }
            }
        }
        return projectNames;
    }

    private static ValidationReport validateResourceSet(XtextResourceSet resourceSet, String focusFile) {
        List<ValidationIssue> issues = new ArrayList<>();
        List<ValidationIssue> infoCandidates = new ArrayList<>();
        Set<String> seenIssueKeys = new HashSet<>();
        Set<String> linesWithProblems = new HashSet<>();
        int infos = 0;
        int errors = 0;
        int warnings = 0;

        for (Resource resource : resourceSet.getResources()) {
            if (!(resource instanceof XtextResource) || !resource.getURI().isPlatformResource()) {
                continue;
            }

            IResourceValidator validator = ((XtextResource) resource).getResourceServiceProvider().getResourceValidator();
            List<Issue> resourceIssues = validator.validate(resource, CheckMode.ALL, CancelIndicator.NullImpl);
            String platformPath = resource.getURI().toPlatformString(true);
            if (!matchesFocusFile(platformPath, focusFile)) {
                continue;
            }
            for (Issue issue : resourceIssues) {
                if (shouldIgnoreIssue(issue)) {
                    continue;
                }
                if (issue.getSeverity() == Severity.ERROR) {
                    errors++;
                    ValidationIssue validationIssue = new ValidationIssue("error", issue.getMessage(),
                            platformPath, safeLine(issue));
                    addDistinctIssue(issues, seenIssueKeys, validationIssue);
                    linesWithProblems.add(problemLineKey(validationIssue.file, validationIssue.line));
                } else if (issue.getSeverity() == Severity.WARNING) {
                    warnings++;
                    ValidationIssue validationIssue = new ValidationIssue("warning", issue.getMessage(),
                            platformPath, safeLine(issue));
                    addDistinctIssue(issues, seenIssueKeys, validationIssue);
                    linesWithProblems.add(problemLineKey(validationIssue.file, validationIssue.line));
                } else if (issue.getSeverity() == Severity.INFO) {
                    infoCandidates.add(new ValidationIssue("info", issue.getMessage(), platformPath, safeLine(issue)));
                }
            }
        }

        for (ValidationIssue infoIssue : infoCandidates) {
            if (linesWithProblems.contains(problemLineKey(infoIssue.file, infoIssue.line))) {
                infos++;
                addDistinctIssue(issues, seenIssueKeys, infoIssue);
            }
        }

        issues.sort(Comparator.comparing((ValidationIssue issue) -> issue.file)
                .thenComparingInt(issue -> issue.line)
                .thenComparing(issue -> issue.severity)
                .thenComparing(issue -> issue.message));
        return new ValidationReport(infos, warnings, errors, issues);
    }

    private static boolean matchesFocusFile(String platformPath, String focusFile) {
        if (focusFile == null || focusFile.isBlank()) {
            return true;
        }

        String normalizedFocus = focusFile.replace("\\", "/").trim();
        String normalizedPath = platformPath.replace("\\", "/");
        return normalizedPath.endsWith("/" + normalizedFocus) || normalizedPath.equals(normalizedFocus);
    }

    private static boolean shouldIgnoreIssue(Issue issue) {
        String message = issue.getMessage();
        if (message == null) {
            return false;
        }

        return message.contains("has duplicates");
    }

    private static String problemLineKey(String file, int line) {
        return file + ":" + line;
    }

    private static void addDistinctIssue(List<ValidationIssue> issues, Set<String> seenIssueKeys, ValidationIssue issue) {
        String key = issue.severity + "|" + issue.file + "|" + issue.line + "|" + issue.message;
        if (seenIssueKeys.add(key)) {
            issues.add(issue);
        }
    }

    private static int safeLine(Issue issue) {
        return issue.getLineNumber() == null ? 0 : issue.getLineNumber();
    }

    private static final class Args {
        private Path workspace;
        private Path project;
        private Path osateHome;
        private Path output;
        private String focusFile;
        private boolean failOnWarning;
        private boolean help;
        private final List<Path> libs = new ArrayList<>();
        private final List<Path> libDirs = new ArrayList<>();

        private static Args parse(String[] args) {
            Args parsed = new Args();
            for (int i = 0; i < args.length; i++) {
                String arg = args[i];
                switch (arg) {
                case "--workspace":
                    parsed.workspace = Paths.get(nextValue(args, ++i, arg));
                    break;
                case "--project":
                    parsed.project = Paths.get(nextValue(args, ++i, arg));
                    break;
                case "--osate-home":
                    parsed.osateHome = Paths.get(nextValue(args, ++i, arg));
                    break;
                case "--output":
                    parsed.output = Paths.get(nextValue(args, ++i, arg));
                    break;
                case "--focus-file":
                    parsed.focusFile = nextValue(args, ++i, arg);
                    break;
                case "--lib":
                    parsed.libs.add(Paths.get(nextValue(args, ++i, arg)));
                    break;
                case "--lib-dir":
                    parsed.libDirs.add(Paths.get(nextValue(args, ++i, arg)));
                    break;
                case "--fail-on-warning":
                    parsed.failOnWarning = true;
                    break;
                case "--help":
                case "-h":
                    parsed.help = true;
                    break;
                default:
                    throw new IllegalArgumentException("Unknown argument: " + arg);
                }
            }
            return parsed;
        }

        private static String nextValue(String[] args, int index, String argName) {
            if (index >= args.length) {
                throw new IllegalArgumentException("Missing value for " + argName);
            }
            return args[index];
        }
    }

    private static final class ValidationReport {
        private final int infos;
        private final int warnings;
        private final int errors;
        private final List<ValidationIssue> issues;

        private ValidationReport(int infos, int warnings, int errors, List<ValidationIssue> issues) {
            this.infos = infos;
            this.warnings = warnings;
            this.errors = errors;
            this.issues = issues;
        }

        private String toJson() {
            StringBuilder builder = new StringBuilder();
            builder.append("{\n");
            builder.append("  \"infos\": ").append(infos).append(",\n");
            builder.append("  \"warnings\": ").append(warnings).append(",\n");
            builder.append("  \"errors\": ").append(errors).append(",\n");
            builder.append("  \"issues\": [");
            if (!issues.isEmpty()) {
                builder.append("\n");
                for (int i = 0; i < issues.size(); i++) {
                    ValidationIssue issue = issues.get(i);
                    builder.append("    ").append(issue.toJson());
                    if (i < issues.size() - 1) {
                        builder.append(",");
                    }
                    builder.append("\n");
                }
                builder.append("  ");
            }
            builder.append("]\n");
            builder.append("}");
            return builder.toString();
        }
    }

    private static final class LoadResult {
        private final String projectName;
        private final Set<String> loadedFileNames;

        private LoadResult(String projectName, Set<String> loadedFileNames) {
            this.projectName = projectName;
            this.loadedFileNames = loadedFileNames;
        }
    }

    private static final class ValidationIssue {
        private final String severity;
        private final String message;
        private final String file;
        private final int line;

        private ValidationIssue(String severity, String message, String file, int line) {
            this.severity = severity;
            this.message = message;
            this.file = file;
            this.line = line;
        }

        private String toJson() {
            return "{"
                    + "\"severity\": \"" + escape(severity) + "\", "
                    + "\"issue\": \"" + escape(message) + "\", "
                    + "\"file\": \"" + escape(file) + "\", "
                    + "\"line\": " + line
                    + "}";
        }
    }

    private static String escape(String value) {
        StringBuilder escaped = new StringBuilder();
        for (int i = 0; i < value.length(); i++) {
            char c = value.charAt(i);
            switch (c) {
            case '\\':
                escaped.append("\\\\");
                break;
            case '"':
                escaped.append("\\\"");
                break;
            case '\b':
                escaped.append("\\b");
                break;
            case '\f':
                escaped.append("\\f");
                break;
            case '\n':
                escaped.append("\\n");
                break;
            case '\r':
                escaped.append("\\r");
                break;
            case '\t':
                escaped.append("\\t");
                break;
            default:
                if (c < 0x20) {
                    escaped.append(String.format("\\u%04x", (int) c));
                } else {
                    escaped.append(c);
                }
            }
        }
        return escaped.toString();
    }
}

