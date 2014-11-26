package hu.bme.mit.pappi.diploma.mondix.model.impl;

import hu.bme.mit.pappi.diploma.mondix.model.ITeiidMondixModel;
import hu.bme.mit.pappi.diploma.mondix.model.TeiidLoadHelper;

import java.util.HashMap;

import com.google.common.collect.ImmutableMap;

import eu.mondo.mondix.core.IMondixInstance;
import eu.mondo.mondix.implementation.hashmap.ImmutableMapRow;
import eu.mondo.mondix.implementation.hashmap.live.ChangeAwareMondixInstance;

/**
 * @author pappi
 *
 */
public class TeiidDemoModelImpl implements ITeiidMondixModel {

	ChangeAwareMondixInstance<ImmutableMapRow> mondixer;

	public TeiidDemoModelImpl() throws Exception {
			mondixer = new ChangeAwareMondixInstance<>(new HashMap(),
					new HashMap());
			initModel();
	}

	@Override
	public IMondixInstance getMondixer() {
		return mondixer;
	}

	public void initModel() {
		mondixer = TeiidLoadHelper.loadRelation(mondixer);
	}

	@Override
	public void performUnaryInsert(String relationName, String column,
			String value) {
		mondixer.addRow(relationName,
				new ImmutableMapRow(ImmutableMap.of(column, value)));
	}

	@Override
	public void performUnaryDelete(String relationName, String column,
			String value) {
		mondixer.removeRow(relationName,
				new ImmutableMapRow(ImmutableMap.of(column, value)));
	}

	@Override
	public void performUnaryUpdate(String relationName, String old_column,
			String old_value, String new_column, String new_value) {
		mondixer.removeRow(relationName,
				new ImmutableMapRow(ImmutableMap.of(old_column, old_value)));
		mondixer.addRow(relationName,
				new ImmutableMapRow(ImmutableMap.of(new_column, new_value)));
	}

	@Override
	public void performBinaryInsert(String relationName, String column1,
			String value1, String column2, String value2) {
		mondixer.addRow(
				relationName,
				new ImmutableMapRow(ImmutableMap.of(column1, value1, column2,
						value2)));
	}

	@Override
	public void performBinaryDelete(String relationName, String column1,
			String value1, String column2, String value2) {
		mondixer.removeRow(
				relationName,
				new ImmutableMapRow(ImmutableMap.of(column1, value1, column2,
						value2)));
	}

	@Override
	public void performBinaryUpdate(String relationName, String old_column1,
			String old_value1, String old_column2, String old_value2,
			String new_column1, String new_value1, String new_column2,
			String new_value2) {
		mondixer.removeRow(
				relationName,
				new ImmutableMapRow(ImmutableMap.of(old_column1, old_value1,
						old_column2, old_value2)));
		mondixer.addRow(
				relationName,
				new ImmutableMapRow(ImmutableMap.of(new_column1, new_value1,
						new_column2, new_value2)));
	}

}
