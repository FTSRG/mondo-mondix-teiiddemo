namespace java hu.bme.mit.pappi.diploma.mondix_change_interface  // define namespace for java code

typedef i32 int

service MondixTeiidChangeService {  // defines service called when Teiid datasource changed

		int performBinaryInsert(1:string relationName, 2:string column1, 3:string column2)
		
		int performBinaryDelete(1:string relationName, 2:string column1, 3:string column2)
		
		int performBinaryUpdate(1:string relationName, 2:string old_column1, 3:string old_column2, 4:string new_column1, 5:string new_column2)
		
		int performUnaryInsert(1:string relationName, 2:string column1)
		
		int performUnaryDelete(1:string relationName, 2:string column1)
		
		int performUnaryUpdate(1:string relationName, 2:string column1)

}