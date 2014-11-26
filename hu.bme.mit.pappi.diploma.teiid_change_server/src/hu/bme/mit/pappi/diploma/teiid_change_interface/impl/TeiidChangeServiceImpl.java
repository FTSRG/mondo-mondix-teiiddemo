package hu.bme.mit.pappi.diploma.teiid_change_interface.impl;

import hu.bme.mit.pappi.diploma.mondix_change_interface.BinaryTuple;
import hu.bme.mit.pappi.diploma.mondix_change_interface.MondixTeiidChangeService;
import hu.bme.mit.pappi.diploma.mondix_change_interface.UnaryTuple;
import hu.bme.mit.pappi.diploma.teiid_change_interface.TeiidChangeService;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.HashMap;

import org.apache.thrift.TException;
import org.apache.thrift.transport.TTransportException;

public class TeiidChangeServiceImpl implements TeiidChangeService.Iface {

	private MondixTeiidChangeService.Client client = null;

	private Connection teiidConnection = null;

	private String SCHEMA_NAME = null;

	private HashMap<String, String> viewPKNames = new HashMap<String, String>();

	public TeiidChangeServiceImpl(MondixTeiidChangeService.Client client,
			Connection conn, String schemaName) throws TTransportException {
		this.client = client;
		this.teiidConnection = conn;
		this.SCHEMA_NAME = schemaName;

		// Initialize VIEW Primary key names
		viewPKNames.put("Activity", "activity_id");
		viewPKNames.put("UserActivity", "activity_id");
		viewPKNames.put("IssueStatusActivity", "activity_id");
		viewPKNames.put("IssueStatusActivityValue", "activity_id");
		viewPKNames.put("Issue", "issue_id");
		viewPKNames.put("IssueSubject", "id");
		viewPKNames.put("ClosedIssueStatuses", "status_id");
		viewPKNames.put("UserLogin", "id");
		viewPKNames.put("User", "id");
	}

	@Override
	public long datasourceChanged(String dsName, String tableName,
			String changeId, String changeType) throws TException {
		(new Thread(new TeiidChangeWorker(dsName, tableName, changeId,
				changeType))).start();
		return 0;
	}

	private class TeiidChangeWorker implements Runnable {

		String dsName;
		String tableName;
		String changeId;
		String changeType;

		public TeiidChangeWorker(String _dsName, String _tableName,
				String _changeId, String _changeType) {
			this.dsName = _dsName;
			this.tableName = _tableName;
			this.changeId = _changeId;
			this.changeType = _changeType;
		}

		@Override
		public void run() {
			try {
				Thread.sleep(2000);
				System.out.println("==DS CHANGE: " + dsName + "|" + tableName
						+ "|" + changeId + "|" + changeType);
				Statement viewsStmnt = teiidConnection.createStatement();
				ResultSet views = viewsStmnt.executeQuery(getModifiedViewSQL(
						dsName, tableName));

				while (views.next()) {

					String relationName = views.getString(1);

					System.out.println("Selected relation (view): "
							+ relationName);

					Statement changedRelStmnt = teiidConnection
							.createStatement();

					ResultSet changedRelation = changedRelStmnt
							.executeQuery(getModifiedTupleSQL(relationName,
									viewPKNames.get(relationName),
									getMappedViewId(changeId)));

					if (changedRelation.next()) {

						int dim = changedRelation.getMetaData()
								.getColumnCount();
						switch (dim) {
						case 1:
							// Unary relation
							UnaryTuple unaryTuple = new UnaryTuple(
									relationName, changedRelation.getMetaData()
											.getColumnName(1),
									changedRelation.getString(1));
							System.out.println("Unary tuple: "
									+ unaryTuple.toString());
							notifyUnaryChange(unaryTuple, changeType);
							break;
						case 2:
							// Binary relation
							BinaryTuple binaryTuple = new BinaryTuple(
									relationName, changedRelation.getMetaData()
											.getColumnName(1),
									changedRelation.getString(1),
									changedRelation.getMetaData()
											.getColumnName(2),
									changedRelation.getString(2));
							System.out.println("Binary tuple: "
									+ binaryTuple.toString());
							notifyBinaryChange(binaryTuple, changeType);
							break;
						default:
							System.out
									.println("Relation is not unary or binary; change notification will not performed: "
											+ relationName);
							break;
						}
					} else {
						System.out.println("No record with id: " + changeId
								+ "; in relation: " + relationName);
					}

					if (!changedRelation.isClosed())
						changedRelation.close();
					if (!changedRelStmnt.isClosed())
						changedRelStmnt.close();
				}

				views.close();
				viewsStmnt.close();

			} catch (Exception ex) {
				System.out.println("Failed to perform datasource change: "
						+ dsName + " | " + tableName + " | " + changeType);
				ex.printStackTrace();

			}

		}

		private void notifyUnaryChange(UnaryTuple tuple, String changeType)
				throws TException {
			switch (changeType) {
			case "INSERT":
				client.performUnaryInsert(tuple);
				break;
			case "DELETE":
				client.performUnaryDelete(tuple);
				break;
			default:
				System.out.println("Unhandled change type: " + changeType);
				break;
			}
		}

		private void notifyBinaryChange(BinaryTuple tuple, String changeType)
				throws TException {
			switch (changeType) {
			case "INSERT":
				client.performBinaryInsert(tuple);
				break;
			case "DELETE":
				client.performBinaryDelete(tuple);
				break;
			default:
				System.out.println("Unhandled change type: " + changeType);
				break;
			}
		}

		private String getMappedViewId(String changeId) {
			// TODO: used in multiply data source
			return changeId;
		}

		private String getModifiedTupleSQL(String relationName, String idName,
				String id) {
			StringBuilder sql = new StringBuilder();

			sql.append("SELECT * FROM ");
			sql.append(SCHEMA_NAME);
			sql.append(".");
			sql.append(relationName);
			sql.append(" WHERE ");
			sql.append(idName);
			sql.append("=");
			sql.append(id);
			sql.append(" OPTION NOCACHE");
			System.out.println(sql.toString());
			return sql.toString();
		}

		private String getModifiedViewSQL(String dsName, String tableName) {
			StringBuilder sql = new StringBuilder();
			sql.append("SELECT Name, Body FROM SYSADMIN.Views v ");
			sql.append("WHERE v.Body LIKE '%");
			sql.append(dsName);
			sql.append(".");
			sql.append(tableName);
			sql.append("%'");
			sql.append(" OPTION NOCACHE");
			System.out.println(sql.toString());
			return sql.toString();
		}
	}

}
