package org.agreeautogen.validator;

import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.eclipse.xtext.util.CancelIndicator;
import org.eclipse.xtext.validation.CheckMode;
import org.eclipse.xtext.validation.IResourceValidator;
import org.eclipse.xtext.validation.Issue;
import org.osate.aadl2.AadlPackage;
import org.osate.aadl2.AnnexSubclause;
import org.osate.aadl2.Classifier;
import org.osate.aadl2.DefaultAnnexSubclause;
import org.osate.aadl2.PublicPackageSection;
import org.osate.annexsupport.AnnexRegistry;
import org.osate.xtext.aadl2.Aadl2StandaloneSetup;

import com.google.inject.Injector;
import com.rockwellcollins.atc.agree.AgreeStandaloneSetup;

public final class InspectAgreeAnnex {
    private InspectAgreeAnnex() {
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            throw new IllegalArgumentException("Usage: InspectAgreeAnnex <aadl-file>");
        }

        Path file = Paths.get(args[0]).toAbsolutePath().normalize();
        Injector injector = new Aadl2StandaloneSetup().createInjectorAndDoEMFRegistration();
        Injector agreeInjector = new AgreeStandaloneSetup().createInjectorAndDoEMFRegistration();

        System.out.println("Registered annex names before manual register: " + AnnexRegistry.getAllAnnexNames());
        AnnexRegistry.registerParser("agree", new StandaloneAgreeAnnexParser(agreeInjector));
        AnnexRegistry.registerLinkingService("agree", new StandaloneAgreeAnnexLinkingService(agreeInjector));
        System.out.println("Registered annex names after manual register: " + AnnexRegistry.getAllAnnexNames());

        XtextResourceSet resourceSet = injector.getInstance(XtextResourceSet.class);
        URI uri = URI.createPlatformResourceURI("Inspect/" + file.getFileName(), true);
        Resource resource = resourceSet.createResource(uri);
        try (InputStream stream = Files.newInputStream(file)) {
            resource.load(stream, Collections.emptyMap());
        }
        EcoreUtil.resolveAll(resourceSet);
        IResourceValidator validator = ((org.eclipse.xtext.resource.XtextResource) resource)
                .getResourceServiceProvider().getResourceValidator();
        List<Issue> issues = validator.validate(resource, CheckMode.ALL, CancelIndicator.NullImpl);
        System.out.println("Validation issue count: " + issues.size());
        for (Issue issue : issues) {
            System.out.println("  [" + issue.getSeverity() + "] " + issue.getMessage());
        }

        EObject root = resource.getContents().get(0);
        System.out.println("Root class: " + root.eClass().getName());
        AadlPackage pkg = (AadlPackage) root;
        PublicPackageSection section = pkg.getOwnedPublicSection();
        for (Classifier classifier : section.getOwnedClassifiers()) {
            System.out.println("Classifier: " + classifier.getQualifiedName());
            List<AnnexSubclause> annexes = classifier.getOwnedAnnexSubclauses();
            for (AnnexSubclause annex : annexes) {
                System.out.println("  Annex object class: " + annex.eClass().getName());
                System.out.println("  Annex name: " + annex.getName());
                printFeature(annex, "parsedAnnexSubclause", "  parsedAnnexSubclause");
                if (annex instanceof DefaultAnnexSubclause) {
                    DefaultAnnexSubclause defaultAnnex = (DefaultAnnexSubclause) annex;
                    System.out.println("  sourceText starts: " + safe(defaultAnnex.getSourceText()));
                }
            }
        }
    }

    private static void printFeature(EObject object, String featureName, String label) {
        EStructuralFeature feature = object.eClass().getEStructuralFeature(featureName);
        if (feature == null) {
            System.out.println(label + ": <no feature>");
            return;
        }
        Object value = object.eGet(feature);
        if (value == null) {
            System.out.println(label + ": null");
            return;
        }
        if (value instanceof EObject) {
            EObject eObject = (EObject) value;
            System.out.println(label + ": " + eObject.eClass().getName() + " (" + eObject.getClass().getName() + ")");
            printFeature(eObject, "contract", "    contract");
        } else {
            System.out.println(label + ": " + value);
        }
    }

    private static String safe(String text) {
        if (text == null) {
            return "null";
        }
        text = text.replace('\r', ' ').replace('\n', ' ').trim();
        return text.length() > 120 ? text.substring(0, 120) + "..." : text;
    }
}

