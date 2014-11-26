package hu.bme.mit.pappi.diploma.mondo_mondix_teiiddemo.test;

import static org.junit.Assert.assertTrue;
import hu.bme.mit.pappi.diploma.mondix_change_interface.BinaryTuple;
import hu.bme.mit.pappi.diploma.mondix_change_interface.MondixTeiidChangeService;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.junit.Before;
import org.junit.Test;

public class MondixTeiidServerTest {

	private final static int SERVER_PORT = 7921;
	private final static String SERVER_IP = "localhost";

	private MondixTeiidChangeService.Client client;

	@Before
	public void setUp() throws Exception {
		TTransport transport = new TSocket(SERVER_IP, SERVER_PORT);

		TProtocol protocol = new TBinaryProtocol(transport);

		client = new MondixTeiidChangeService.Client(protocol);

		transport.open();
	}

	@Test
	public void testInsert() throws TException {

		long matchNum = client.getMatchesCount(getTeiidMondixQuerySource());
		
		System.out.println("Matches number: " + matchNum);
		
		assertTrue(matchNum > 0);
		
		client.performBinaryInsert(new BinaryTuple("UserLogin", "id", String.valueOf(matchNum), "login", "arzivturo"));
		
		matchNum = client.getMatchesCount(getTeiidMondixQuerySource());
		
		System.out.println("Matches number: " + matchNum);
		
		assertTrue(matchNum > 0);
	}

	private final static String getTeiidMondixQuerySource() {

		StringBuilder mondixQuery = new StringBuilder();

		mondixQuery.append("pattern teiidMondixQuery(x, y) {");
		mondixQuery.append("UserLogin(x, y);");
		mondixQuery.append("}");

		return mondixQuery.toString();
	}

}
