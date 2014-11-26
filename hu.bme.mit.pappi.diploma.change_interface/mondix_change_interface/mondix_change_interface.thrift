namespace java hu.bme.mit.pappi.diploma.mondix_change_interface  // define namespace for java code

typedef i32 int
typedef i64 long

struct UnaryTuple {
  1: string relationName,
  2: string column,
  3: string value,
}

struct BinaryTuple {
  1: string relationName,
  2: string column1,
  3: string value1,
  4: string column2,
  5: string value2
}

service MondixTeiidChangeService {  // defines service called when Teiid datasource changed

		int performBinaryInsert(1:BinaryTuple tuple)
		
		int performBinaryDelete(1:BinaryTuple tuple)
		
		int performBinaryUpdate(1:BinaryTuple oldTuple, 2:BinaryTuple newTuple)
		
		int performUnaryInsert(1:UnaryTuple tuple)
		
		int performUnaryDelete(1:UnaryTuple tuple)
		
		int performUnaryUpdate(1:UnaryTuple oldTuple, 2:UnaryTuple newTuple)
		
		long getMatchesCount(1:string query)		

}