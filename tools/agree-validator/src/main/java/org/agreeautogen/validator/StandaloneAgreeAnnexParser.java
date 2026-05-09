package org.agreeautogen.validator;

import org.osate.aadl2.AnnexLibrary;
import org.osate.aadl2.AnnexSubclause;
import org.osate.annexsupport.AnnexParseUtil;
import org.osate.annexsupport.AnnexParser;
import org.osate.aadl2.modelsupport.errorreporting.ParseErrorReporter;

import com.google.inject.Injector;
import com.rockwellcollins.atc.agree.parser.antlr.AgreeParser;
import com.rockwellcollins.atc.agree.services.AgreeGrammarAccess;

public final class StandaloneAgreeAnnexParser implements AnnexParser {
    private final Injector injector;
    private AgreeParser parser;

    public StandaloneAgreeAnnexParser(Injector injector) {
        this.injector = injector;
    }

    private AgreeParser getParser() {
        if (parser == null) {
            parser = injector.getInstance(AgreeParser.class);
        }
        return parser;
    }

    private AgreeGrammarAccess getGrammarAccess() {
        return getParser().getGrammarAccess();
    }

    @Override
    public AnnexLibrary parseAnnexLibrary(String annexName, String source, String filename, int line, int column,
            ParseErrorReporter errReporter) {
        return (AnnexLibrary) AnnexParseUtil.parse(getParser(), source, getGrammarAccess().getAgreeLibraryRule(),
                filename, line, column, errReporter);
    }

    @Override
    public AnnexSubclause parseAnnexSubclause(String annexName, String source, String filename, int line, int column,
            ParseErrorReporter errReporter) {
        return (AnnexSubclause) AnnexParseUtil.parse(getParser(), source, getGrammarAccess().getAgreeSubclauseRule(),
                filename, line, column, errReporter);
    }

    @Override
    public String getFileExtension() {
        return "agree";
    }
}

