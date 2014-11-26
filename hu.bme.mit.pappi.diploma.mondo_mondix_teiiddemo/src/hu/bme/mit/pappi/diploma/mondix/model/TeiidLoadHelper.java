package hu.bme.mit.pappi.diploma.mondix.model;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

import com.google.common.collect.ImmutableMap;

import eu.mondo.mondix.implementation.hashmap.ImmutableMapRow;
import eu.mondo.mondix.implementation.hashmap.live.ChangeAwareMondixInstance;

/**
 * @author pappi
 */
public class TeiidLoadHelper {

	private static final String VDB_URL = "jdbc:teiid:DiplomaVDB.1@mm://teiid:31000";
	private static final String VDB_USER = "user";
	private static final String VDB_PASSWORD = "Teiid/12345";
	private static final String DATABASE_NAME = "DiplomaVDB";
	private static final String SCHEMA_NAME = "ManagementViews";

	private static Connection teiidConnection = null;

	public static Connection initTeiidConnection() {
		try {
//			if ((teiidConnection != null) && (!teiidConnection.isClosed()))
//				return teiidConnection;
//			else

				teiidConnection = DriverManager.getConnection(VDB_URL,
						VDB_USER, VDB_PASSWORD);
		} catch (SQLException e) {
			System.out.println("Unable to create connection to Teiid Server!");
			e.printStackTrace();
		}
		
		return teiidConnection;
	}

	public static void closeTeiidConnection() {
		try {
			if (teiidConnection != null && !teiidConnection.isClosed())
				teiidConnection.close();
		} catch (SQLException ex) {
			System.out
					.println("Something wrong happened while closing Teiid connection!");
			ex.printStackTrace();
		}
	}

	public static ChangeAwareMondixInstance<ImmutableMapRow> loadRelation(
			ChangeAwareMondixInstance<ImmutableMapRow> mondixer) {
		System.out.println("Loading model from Teiid server ... ");

		initTeiidConnection();
		try {

			ResultSet relations = teiidConnection.getMetaData().getTables(
					DATABASE_NAME, SCHEMA_NAME, "%", null);

			ArrayList<String> relationNames = new ArrayList<String>();
			while (relations.next()) {
				relationNames.add(relations.getString(3));
			}

			for (String relationName : relationNames) {
				Statement statement = teiidConnection.createStatement();
				String sqlQuery = getQueryToLoad(relationName);
				System.out.println("Query string: " + sqlQuery);
				ResultSet results = statement.executeQuery(sqlQuery);
				ResultSetMetaData md = results.getMetaData();
				int columnCount = md.getColumnCount();
				System.out.println("Column count: " + columnCount);

				switch (columnCount) {
				case 1:
					mondixer.addRelation(relationName,
							new HashSet<ImmutableMapRow>(),
							Arrays.asList(md.getColumnName(1)));
					while (results.next()) {
						mondixer.addRow(
								relationName,
								new ImmutableMapRow(ImmutableMap.of(
										md.getColumnLabel(1),
										results.getString(1))));
					}
					break;
				case 2:
					mondixer.addRelation(
							relationName,
							new HashSet<ImmutableMapRow>(),
							Arrays.asList(md.getColumnName(1),
									md.getColumnName(2)));
					while (results.next()) {
						mondixer.addRow(
								relationName,
								new ImmutableMapRow(ImmutableMap.of(
										md.getColumnLabel(1),
										results.getString(1),
										md.getColumnLabel(2),
										results.getString(2))));
					}
					break;
				default:
					// TODO: handle it smartly.
					System.out
							.println("Relation column number is greater than 2 - skipped!");
					continue;
				}

				results.close();
				statement.close();
			}
		} catch (SQLException e) {
			e.printStackTrace();

		}
		closeTeiidConnection();
		return mondixer;
	}

	private static String getQueryToLoad(String _relName) {
		StringBuilder query = new StringBuilder();
		query.append("SELECT * FROM ");
		query.append(SCHEMA_NAME);
		query.append(".");
		query.append(_relName);
		// query.append(" WHERE login <> ''");
		return query.toString();
	}
}
