package org.agreeautogen.validator;

import java.util.List;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.xtext.linking.ILinkingService;
import org.eclipse.xtext.naming.IQualifiedNameProvider;
import org.eclipse.xtext.naming.QualifiedName;
import org.eclipse.xtext.nodemodel.INode;
import org.osate.annexsupport.AnnexLinkingService;

import com.google.inject.Injector;
import com.rockwellcollins.atc.agree.linking.AgreeLinkingService;

public final class StandaloneAgreeAnnexLinkingService implements AnnexLinkingService {
    private final Injector injector;
    private ILinkingService linkingService;
    private IQualifiedNameProvider nameProvider;

    public StandaloneAgreeAnnexLinkingService(Injector injector) {
        this.injector = injector;
    }

    private ILinkingService getLinkingService() {
        if (linkingService == null) {
            linkingService = injector.getInstance(AgreeLinkingService.class);
        }
        return linkingService;
    }

    private IQualifiedNameProvider getNameProvider() {
        if (nameProvider == null) {
            nameProvider = injector.getInstance(IQualifiedNameProvider.class);
        }
        return nameProvider;
    }

    @Override
    public List<EObject> resolveAnnexReference(String annexName, EObject context, EReference reference, INode node) {
        return getLinkingService().getLinkedObjects(context, reference, node);
    }

    @Override
    public QualifiedName getFullyQualifiedName(EObject obj) {
        return getNameProvider().getFullyQualifiedName(obj);
    }
}

