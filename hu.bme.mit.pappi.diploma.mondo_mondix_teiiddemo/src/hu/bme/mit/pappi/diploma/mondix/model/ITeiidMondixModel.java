package hu.bme.mit.pappi.diploma.mondix.model;

import eu.mondo.mondix.core.IMondixInstance;

public interface ITeiidMondixModel {

	public IMondixInstance getMondixer();
	
	public void performUnaryInsert(String relationName, String column,
			String value);

	public void performUnaryDelete(String relationName, String column,
			String value);

	public void performUnaryUpdate(String relationName, String old_column,
			String old_value, String new_column, String new_value);

	public void performBinaryInsert(String relationName, String column1,
			String value1, String column2, String value2);

	public void performBinaryDelete(String relationName, String column1,
			String value1, String column2, String value2);

	public void performBinaryUpdate(String relationName, String old_column1,
			String old_value1, String old_column2, String old_value2,
			String new_column1, String new_value1, String new_column2,
			String new_value2);
}
