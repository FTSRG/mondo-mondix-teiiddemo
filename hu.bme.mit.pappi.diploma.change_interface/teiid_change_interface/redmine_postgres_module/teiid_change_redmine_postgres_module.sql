-- Add procedural language to database
CREATE OR REPLACE PROCEDURAL LANGUAGE 'plpythonu' HANDLER plpython_call_handler;

-- DROP teiid_notify_change function, if already exists
DROP FUNCTION IF EXISTS teiid_notify_change(
	dsName text,
	tableName text,
	changeId text,
	changeType text);

-- Define teiid_notify_change function
CREATE OR REPLACE FUNCTION teiid_notify_change(
	dsName text,
	tableName text,
	changeId text,
	changeType text) RETURNS text AS
$$

dsName = args[0]
tableName = args[1]
changeId = args[2]
changeType = args[3]

import sys
import os

from sys import path

path.append(os.environ['TEIID_CHANGE_HOME'])

from teiid_change_interface import TeiidChangeService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

  # Make socket
  transport = TSocket.TSocket('192.168.56.1', 7911)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = TeiidChangeService.Client(protocol)

  # Connect!
  transport.open()

  # Notify Teiid change server from the change. Return 0 if it was successfull.
  # TODO: handle the case when server is not available:
  # - send notify that data is dirty -> perform reinicialization
  # - collect changes to a table, and send them when server is up again.
  product = client.datasourceChanged(dsName, tableName, changeId, changeType)

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)

$$
LANGUAGE 'plpythonu';

-- Test the function
-- select teiid_notify_change('RedmineDS', 'TestTable', '12345', 'INSERT');

-- Create trigger(s) on tables, which are relevant by the KPI(s)
CREATE OR REPLACE FUNCTION journals_change() RETURNS trigger AS
$journal_change$
DECLARE
	table_name text := TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME;
	change_id text := '';
	datasource text := 'RedmineDS';
BEGIN
    CASE TG_OP
        WHEN 'INSERT', 'UPDATE' THEN
            change_id := NEW.id;
            PERFORM teiid_notify_change(datasource, table_name, change_id, TG_OP);
            RETURN NEW;
        WHEN 'DELETE' THEN
            change_id := OLD.id;
            PERFORM teiid_notify_change('RedmineDS', table_name, change_id, TG_OP);
            RETURN OLD;
        ELSE
            RAISE EXCEPTION 'Unknown TG_OP: "%" Should not occur!', TG_OP;
    END CASE;
END;
$journal_change$
LANGUAGE PLPGSQL;

DROP TRIGGER IF EXISTS journals_change_trigger ON journals;
CREATE TRIGGER journals_change_trigger 
AFTER INSERT ON journals
FOR EACH ROW
EXECUTE PROCEDURE journals_change();

