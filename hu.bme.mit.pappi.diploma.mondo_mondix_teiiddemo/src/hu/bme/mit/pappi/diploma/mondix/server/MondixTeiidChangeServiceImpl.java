package hu.bme.mit.pappi.diploma.mondix.server;

import hu.bme.mit.pappi.diploma.mondix.model.ITeiidMondixModel;
import hu.bme.mit.pappi.diploma.mondix.parser.StandaloneMondixParser;
import hu.bme.mit.pappi.diploma.mondix_change_interface.BinaryTuple;
import hu.bme.mit.pappi.diploma.mondix_change_interface.MondixTeiidChangeService;
import hu.bme.mit.pappi.diploma.mondix_change_interface.UnaryTuple;

import org.apache.thrift.TException;
import org.eclipse.incquery.patternlanguage.mondix.mondixPatternLanguage.MondixPatternModel;
import org.eclipse.incquery.patternlanguage.mondix.psystem.MondixPModel;
import org.eclipse.incquery.patternlanguage.util.psystem.GenericPQuery;
import org.eclipse.incquery.runtime.api.GenericPatternMatch;
import org.eclipse.incquery.runtime.api.IncQueryMatcher;

public class MondixTeiidChangeServiceImpl implements
		MondixTeiidChangeService.Iface {

	ITeiidMondixModel model;

	StandaloneMondixParser parser;
	
	public MondixTeiidChangeServiceImpl(ITeiidMondixModel model) {
		this.model = model;
		parser = new StandaloneMondixParser();
	}

	@Override
	public int performBinaryInsert(BinaryTuple tuple) throws TException {
		try {
			model.performBinaryInsert(tuple.getRelationName(),
					tuple.getColumn1(), tuple.getValue1(), tuple.getColumn2(),
					tuple.getValue2());
			System.out.println("Binary INSERT performed: " + tuple);
		} catch (Exception e) {
			System.out.println("Binary INSERT failed: "
					+ tuple);
			e.printStackTrace();
			return -1;
		}
		return 0;
	}

	@Override
	public int performBinaryDelete(BinaryTuple tuple) throws TException {
		try {
			model.performBinaryDelete(tuple.getRelationName(),
					tuple.getColumn1(), tuple.getValue1(),
					tuple.getColumn2(), tuple.getValue2());
			System.out.println("Binary DELETE performed: " + tuple.toString());
		} catch (Exception e) {
			System.out.println("Binary DELETE failed: "
					+ tuple.toString());
			e.printStackTrace();
			return -1;
		}
		return 0;
	}

	@Override
	public int performBinaryUpdate(BinaryTuple oldTuple, BinaryTuple newTuple)
			throws TException {
		if (!oldTuple.getRelationName().equals(newTuple.getRelationName())) {
			System.out.println("Binary UPDATE failed: " + oldTuple.getRelationName());
			System.out.println("Relation names are different!");
			return -1;
		}
		try {
			model.performBinaryUpdate(oldTuple.getRelationName(),
					oldTuple.getColumn1(), oldTuple.getValue1(),
					oldTuple.getColumn2(), oldTuple.getValue2(),
					newTuple.getColumn1(), newTuple.getValue1(),
					newTuple.getColumn2(), newTuple.getValue2());
			System.out.println("Binary UPDATE performed: OLD:\n" + oldTuple);
			System.out.println("NEW: " + newTuple);
		} catch (Exception e) {
			System.out.println("Binary UPDATE failed: "
					+ oldTuple);
			e.printStackTrace();
			return -1;
		}
		return 0;
	}

	@Override
	public int performUnaryInsert(UnaryTuple tuple) throws TException {
		try {
			model.performUnaryInsert(tuple.getRelationName(),
					tuple.getColumn(), tuple.getValue());
			System.out.println("Unary INSERT performed: " + tuple);
		} catch (Exception e) {
			System.out.println("Unary INSERT failed: "
					+ tuple);
			e.printStackTrace();
			return -1;
		}
		return 0;
	}

	@Override
	public int performUnaryDelete(UnaryTuple tuple) throws TException {
		try {
			model.performUnaryDelete(tuple.getRelationName(),
					tuple.getColumn(), tuple.getValue());
			System.out.println("Unary DELETE performed: " + tuple);
		} catch (Exception e) {
			System.out.println("Unary DELETE failed: " + 
					tuple);
			e.printStackTrace();
		}
		return 0;
	}

	@Override
	public int performUnaryUpdate(UnaryTuple oldTuple, UnaryTuple newTuple)
			throws TException {
		if (!oldTuple.getRelationName().equals(newTuple.getRelationName())) {
			System.out.println("Unary UPDATE failed: " + oldTuple.getRelationName());
			System.out.println("Relation names are different!");
			return -1;
		}
		try {
			model.performUnaryUpdate(oldTuple.getRelationName(),
					oldTuple.getColumn(), oldTuple.getValue(),
					newTuple.getColumn(), newTuple.getValue());
			System.out.println("Unary UPDATE performed in relation " + oldTuple.getRelationName());
		} catch (Exception e) {
			System.out.println("Unary UPDATE failed: " + oldTuple.getRelationName());
			e.printStackTrace();
			return -1;
		}
		return 0;
	}

	@Override
	public long getMatchesCount(String queryString) {
		try {
			MondixPatternModel patternModel = (MondixPatternModel) this.parser
					.parse(queryString);
			
//			Resource _eResource = patternModel.eResource();
//			EList<Resource.Diagnostic> _errors = _eResource.getErrors();
//			boolean _isEmpty = _errors.isEmpty();
//			if(!_isEmpty) {
//				System.out.println("Query parser error: ");
//				for(Resource.Diagnostic diag : _errors)
//					System.out.println("Parser error: " + diag.getMessage());
//				return -1;
//			}
//			
			MondixPModel pModelXform = new MondixPModel(patternModel);
			GenericPQuery query = pModelXform.findQueryOf(patternModel
					.getPatterns().get(0));
			
			IncQueryMatcher<GenericPatternMatch> matcher = ServerMain.getMatcher(query);
			
			return matcher.countMatches();
			
		} catch (Exception e) {
			System.out.println("Count matches failed: " + e.getMessage());
			e.printStackTrace();
			return -1;
		}
		
	}

}
