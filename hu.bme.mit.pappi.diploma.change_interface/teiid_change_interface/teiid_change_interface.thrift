namespace java hu.bme.mit.pappi.diploma.teiid_change_interface  // define namespace for java code

typedef i64 long

service TeiidChangeService {  // defines service called when Teiid datasource changed
		long datasourceChanged(1:string dsName, 2:string tableName, 3:string changeId, 4:string changeType)
}