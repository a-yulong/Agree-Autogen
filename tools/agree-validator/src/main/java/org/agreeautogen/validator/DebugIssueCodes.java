package org.agreeautogen.validator;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.xtext.resource.XtextResource;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.eclipse.xtext.util.CancelIndicator;
import org.eclipse.xtext.validation.CheckMode;
import org.eclipse.xtext.validation.IResourceValidator;
import org.eclipse.xtext.validation.Issue;

import com.google.inject.Injector;
import com.rockwellcollins.atc.agree.AgreeStandaloneSetup;

import org.osate.xtext.aadl2.Aadl2StandaloneSetup;

public final class DebugIssueCodes {
    private DebugIssueCodes() {
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 3) {
            throw new IllegalArgumentException("Usage: DebugIssueCodes <workspace> <project> <osateHome>");
        }

        Path workspace = Paths.get(args[0]).toAbsolutePath().normalize();
        Path project = Paths.get(args[1]).toAbsolutePath().normalize();
        Path osateHome = Paths.get(args[2]).toAbsolutePath().normalize();

        Injector aadlInjector = new Aadl2StandaloneSetup().createInjectorAndDoEMFRegistration();
        Injector agreeInjector = new AgreeStandaloneSetup().createInjectorAndDoEMFRegistration();
        var registerMethod = AgreeValidationCli.class.getDeclaredMethod("registerAgreeAnnexSupport", Injector.class);
        registerMethod.setAccessible(true);
        registerMethod.invoke(null, agreeInjector);

        XtextResourceSet resourceSet = aadlInjector.getInstance(XtextResourceSet.class);
        var loadProjectMethod = AgreeValidationCli.class.getDeclaredMethod("loadProjectAadlFiles", Path.class,
                Path.class, List.class, XtextResourceSet.class);
        loadProjectMethod.setAccessible(true);
        Object loadResult = loadProjectMethod.invoke(null, workspace, project, List.of(), resourceSet);
        var field = loadResult.getClass().getDeclaredField("loadedFileNames");
        field.setAccessible(true);
        @SuppressWarnings("unchecked")
        var loadedFileNames = (java.util.Set<String>) field.get(loadResult);
        var loadResourcesMethod = AgreeValidationCli.class.getDeclaredMethod("loadContributedResources", Path.class,
                java.util.Set.class, org.eclipse.emf.ecore.resource.ResourceSet.class);
        loadResourcesMethod.setAccessible(true);
        loadResourcesMethod.invoke(null, osateHome, loadedFileNames, resourceSet);
        EcoreUtil.resolveAll(resourceSet);

        for (var resource : resourceSet.getResources()) {
            if (!(resource instanceof XtextResource) || !resource.getURI().isPlatformResource()) {
                continue;
            }
            IResourceValidator validator = ((XtextResource) resource).getResourceServiceProvider().getResourceValidator();
            List<Issue> resourceIssues = validator.validate(resource, CheckMode.ALL, CancelIndicator.NullImpl);
            for (Issue issue : resourceIssues) {
                System.out.printf("%s | %s | %s | line %s | %s%n",
                        issue.getSeverity(),
                        issue.getCode(),
                        resource.getURI().toPlatformString(true),
                        issue.getLineNumber(),
                        issue.getMessage());
            }
        }
    }
}

