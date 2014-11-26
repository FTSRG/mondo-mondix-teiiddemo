package hu.bme.mit.pappi.diploma.mondo_mondix_teiiddemo.test;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.ResultSet;
import java.sql.SQLException;

import hu.bme.mit.pappi.diploma.mondix.model.TeiidLoadHelper;

import org.junit.Test;

public class TeiidConnectionTest {
	
	private String DATABASE_NAME = "DiplomaVDB";
	private String SCHEMA_NAME = "ManagementViews";
	
	@Test
	public void testConnection() throws SQLException {
		Connection conn = TeiidLoadHelper.initTeiidConnection();
		
		DatabaseMetaData md = conn.getMetaData();
		
		ResultSet rs = md.getTables(DATABASE_NAME, SCHEMA_NAME, "%", null);
		
		while (rs.next()) {
			System.out.println(rs.getString(3));
		}

		TeiidLoadHelper.closeTeiidConnection();
	}
	
	@Test
	public void testReadData() {
		//TeiidLoadHelper.loadRelation("UserLogin");
	}

	
	
}
