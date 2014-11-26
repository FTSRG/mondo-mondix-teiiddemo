package hu.bme.mit.pappi.diploma.mondix.parser;

import java.io.StringReader;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.incquery.patternlanguage.mondix.MondixPatternLanguageStandaloneSetup;
import org.eclipse.xtext.parser.IParseResult;
import org.eclipse.xtext.parser.IParser;
import org.eclipse.xtext.parser.ParseException;
import org.eclipse.xtext.resource.impl.BinaryGrammarResourceFactoryImpl;

import com.google.inject.Inject;
import com.google.inject.Injector;

/**
 * 
 * @author pappi
 *
 */
public class StandaloneMondixParser {
	
	@Inject
	private IParser parser;
	
	public StandaloneMondixParser() {
		setupParser();
	}
	
	private void setupParser() {
		if (!Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().containsKey("xtextbin"))
			  Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().put(
			                "xtextbin", new BinaryGrammarResourceFactoryImpl());
		Injector injector = new MondixPatternLanguageStandaloneSetup().createInjector();
		injector.injectMembers(this);
	}
	
	public EObject parse(String input) {
		
		IParseResult result = parser.parse(new StringReader(input));
		if(result.hasSyntaxErrors())
        {
            throw new ParseException("Provided input contains syntax errors.");
        }
        return result.getRootASTElement();
	}
	
}
