package hu.bme.mit.pappi.diploma.teiid_change_server;

import hu.bme.mit.pappi.diploma.mondix_change_interface.MondixTeiidChangeService;
import hu.bme.mit.pappi.diploma.teiid_change_interface.TeiidChangeService;
import hu.bme.mit.pappi.diploma.teiid_change_interface.TeiidChangeService.Processor;
import hu.bme.mit.pappi.diploma.teiid_change_interface.impl.TeiidChangeServiceImpl;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadPoolServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

public class ServerMain {

	private final static int MONDIX_SERVER_PORT = 7921;
	private final static String MONDIX_SERVER_IP = "localhost";

	public static final String VDB_URL = "jdbc:teiid:DiplomaVDB.1@mm://teiid:31000";
	public static final String VDB_USER = "user";
	public static final String VDB_PASSWORD = "Teiid/12345";
	public static final String SCHEMA_NAME = "ManagementViews";

	private static final int LOCAL_SERVER_PORT = 7911;

	private MondixTeiidChangeService.Client client = null;

	private TTransport transport = null;

	private Connection teiidConnection = null;

	private void start() throws TTransportException {

		TServerSocket serverTransport = new TServerSocket(LOCAL_SERVER_PORT);

		Processor<TeiidChangeServiceImpl> processor = new TeiidChangeService.Processor<>(
				new TeiidChangeServiceImpl(client, teiidConnection, SCHEMA_NAME));

		TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(
				serverTransport).processor(processor));

		System.out.println("Starting Teiid change server on port "
				+ LOCAL_SERVER_PORT + " ...");

		server.serve();

	}

	private void initTeiidConnection() throws SQLException {
		System.out.println("Initialize Teiid server connection ... ");
		teiidConnection = DriverManager.getConnection(VDB_URL, VDB_USER,
				VDB_PASSWORD);
	}

	private void closeTeiidConnection() throws SQLException {

		if (teiidConnection != null && !teiidConnection.isClosed())
			teiidConnection.close();
	}

	private void initMondixConnection() throws TTransportException {
		System.out.println("Initialize Mondix server connection ... ");
		transport = new TSocket(MONDIX_SERVER_IP, MONDIX_SERVER_PORT);

		TProtocol protocol = new TBinaryProtocol(transport);

		client = new MondixTeiidChangeService.Client(protocol);

		transport.open();
	}

	private void closeMondixConnection() {
		if (transport != null && transport.isOpen())
			transport.close();
	}

	public static void main(String[] args) {
		try {
			ServerMain server = new ServerMain();

			server.initMondixConnection();
			server.initTeiidConnection();

			server.start();
		} catch (Exception e) {
			System.out.println("Unable to start Teiid change server: "
					+ e.getMessage());
			e.printStackTrace();
		}
	}
}
