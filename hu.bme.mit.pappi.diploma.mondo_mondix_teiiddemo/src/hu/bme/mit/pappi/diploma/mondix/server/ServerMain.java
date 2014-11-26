package hu.bme.mit.pappi.diploma.mondix.server;

import hu.bme.mit.pappi.diploma.mondix.model.ITeiidMondixModel;
import hu.bme.mit.pappi.diploma.mondix.model.impl.TeiidDemoModelImpl;
import hu.bme.mit.pappi.diploma.mondix_change_interface.MondixTeiidChangeService;

import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadPoolServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TTransportException;
import org.eclipse.incquery.runtime.api.IPatternMatch;
import org.eclipse.incquery.runtime.api.IQuerySpecification;
import org.eclipse.incquery.runtime.api.IncQueryEngine;
import org.eclipse.incquery.runtime.api.IncQueryMatcher;
import org.eclipse.incquery.runtime.exception.IncQueryException;

import eu.mondo.mondix.incquery.MondixScope;

public class ServerMain {

	private static final int SERVER_PORT = 7921;

	private static IncQueryEngine engine = null;
	
	private void start() {

		try {
			
			ITeiidMondixModel teiidMondixModel = new TeiidDemoModelImpl();
			MondixScope scope = new MondixScope(teiidMondixModel.getMondixer());
			engine = IncQueryEngine.on(scope);

			TServerSocket serverTransport = new TServerSocket(SERVER_PORT);

			MondixTeiidChangeService.Processor<MondixTeiidChangeServiceImpl> processor = new MondixTeiidChangeService.Processor<MondixTeiidChangeServiceImpl>(
					new MondixTeiidChangeServiceImpl(teiidMondixModel));

			TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(
					serverTransport).processor(processor));

			System.out.println("Starting Mondix demo server on port " + SERVER_PORT
					+ " ...");

			server.serve();

		} catch (TTransportException te) {
			System.out.println("Thrift exception in Teiid Mondix server!");
			te.printStackTrace();
		} catch (IncQueryException e) {
			System.out.println("IQ exception in Teiid Mondix server!");
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static <Match extends IPatternMatch> IncQueryMatcher<Match> getMatcher(
			IQuerySpecification<? extends IncQueryMatcher<Match>> query)
			throws IncQueryException {
		IncQueryMatcher<Match> matcher = engine.getMatcher(query);
		return matcher;
		
	}

	public static void main(String[] args) {
		ServerMain server = new ServerMain();

		server.start();
	}

}
