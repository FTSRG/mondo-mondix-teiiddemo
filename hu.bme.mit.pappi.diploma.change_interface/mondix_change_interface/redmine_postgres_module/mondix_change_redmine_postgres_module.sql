-- Add procedural language to database
CREATE OR REPLACE PROCEDURAL LANGUAGE 'plpythonu' HANDLER plpython_call_handler;

-- DROP mondix_perform_binary_insert function, if already exists
DROP FUNCTION IF EXISTS mondix_perform_binary_insert (
	relationName text,
	column1 text,
	column2 text);

-- Define teiid_perform_binary_insert function
CREATE OR REPLACE FUNCTION mondix_perform_binary_insert (
	relationName text,
	column1 text,
	column2 text) RETURNS text AS
$$

relationName = args[0]
column1 = args[1]
column2 = args[2]

import sys
import os

from sys import path

path.append(os.environ['TEIID_CHANGE_HOME'])

from mondix_change_interface import MondixTeiidChangeService
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
  client = MonixTeiidChangeService.Client(protocol)

  # Connect!
  transport.open()

  # Notify Teiid change server from the change. Return 0 if it was successfull.
  # TODO: handle the case when server is not available:
  # - send notify that data is dirty -> perform reinicialization
  # - collect changes to a table, and send them when server is up again.
  product = client.performBinaryInsert(dsName, tableName, changeId, changeType)

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

DROP TRIGGER IF EXISTS journals_insert_trigger ON journals;
CREATE TRIGGER journals_insert_trigger 
AFTER INSERT ON journals
FOR EACH ROW
EXECUTE PROCEDURE journals_change();

DROP TRIGGER IF EXISTS journals_update_trigger ON journals;
CREATE TRIGGER journals_update_trigger
AFTER UPDATE ON journals
FOR EACH ROW 
EXECUTE PROCEDURE journals_change();