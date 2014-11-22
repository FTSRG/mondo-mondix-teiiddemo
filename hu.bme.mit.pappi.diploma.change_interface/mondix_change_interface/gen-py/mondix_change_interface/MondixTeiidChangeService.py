#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def performBinaryInsert(self, relationName, column1, column2):
    """
    Parameters:
     - relationName
     - column1
     - column2
    """
    pass

  def performBinaryDelete(self, relationName, column1, column2):
    """
    Parameters:
     - relationName
     - column1
     - column2
    """
    pass

  def performBinaryUpdate(self, relationName, old_column1, old_column2, new_column1, new_column2):
    """
    Parameters:
     - relationName
     - old_column1
     - old_column2
     - new_column1
     - new_column2
    """
    pass

  def performUnaryInsert(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    pass

  def performUnaryDelete(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    pass

  def performUnaryUpdate(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def performBinaryInsert(self, relationName, column1, column2):
    """
    Parameters:
     - relationName
     - column1
     - column2
    """
    self.send_performBinaryInsert(relationName, column1, column2)
    return self.recv_performBinaryInsert()

  def send_performBinaryInsert(self, relationName, column1, column2):
    self._oprot.writeMessageBegin('performBinaryInsert', TMessageType.CALL, self._seqid)
    args = performBinaryInsert_args()
    args.relationName = relationName
    args.column1 = column1
    args.column2 = column2
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performBinaryInsert(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performBinaryInsert_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performBinaryInsert failed: unknown result");

  def performBinaryDelete(self, relationName, column1, column2):
    """
    Parameters:
     - relationName
     - column1
     - column2
    """
    self.send_performBinaryDelete(relationName, column1, column2)
    return self.recv_performBinaryDelete()

  def send_performBinaryDelete(self, relationName, column1, column2):
    self._oprot.writeMessageBegin('performBinaryDelete', TMessageType.CALL, self._seqid)
    args = performBinaryDelete_args()
    args.relationName = relationName
    args.column1 = column1
    args.column2 = column2
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performBinaryDelete(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performBinaryDelete_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performBinaryDelete failed: unknown result");

  def performBinaryUpdate(self, relationName, old_column1, old_column2, new_column1, new_column2):
    """
    Parameters:
     - relationName
     - old_column1
     - old_column2
     - new_column1
     - new_column2
    """
    self.send_performBinaryUpdate(relationName, old_column1, old_column2, new_column1, new_column2)
    return self.recv_performBinaryUpdate()

  def send_performBinaryUpdate(self, relationName, old_column1, old_column2, new_column1, new_column2):
    self._oprot.writeMessageBegin('performBinaryUpdate', TMessageType.CALL, self._seqid)
    args = performBinaryUpdate_args()
    args.relationName = relationName
    args.old_column1 = old_column1
    args.old_column2 = old_column2
    args.new_column1 = new_column1
    args.new_column2 = new_column2
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performBinaryUpdate(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performBinaryUpdate_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performBinaryUpdate failed: unknown result");

  def performUnaryInsert(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    self.send_performUnaryInsert(relationName, column1)
    return self.recv_performUnaryInsert()

  def send_performUnaryInsert(self, relationName, column1):
    self._oprot.writeMessageBegin('performUnaryInsert', TMessageType.CALL, self._seqid)
    args = performUnaryInsert_args()
    args.relationName = relationName
    args.column1 = column1
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performUnaryInsert(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performUnaryInsert_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performUnaryInsert failed: unknown result");

  def performUnaryDelete(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    self.send_performUnaryDelete(relationName, column1)
    return self.recv_performUnaryDelete()

  def send_performUnaryDelete(self, relationName, column1):
    self._oprot.writeMessageBegin('performUnaryDelete', TMessageType.CALL, self._seqid)
    args = performUnaryDelete_args()
    args.relationName = relationName
    args.column1 = column1
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performUnaryDelete(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performUnaryDelete_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performUnaryDelete failed: unknown result");

  def performUnaryUpdate(self, relationName, column1):
    """
    Parameters:
     - relationName
     - column1
    """
    self.send_performUnaryUpdate(relationName, column1)
    return self.recv_performUnaryUpdate()

  def send_performUnaryUpdate(self, relationName, column1):
    self._oprot.writeMessageBegin('performUnaryUpdate', TMessageType.CALL, self._seqid)
    args = performUnaryUpdate_args()
    args.relationName = relationName
    args.column1 = column1
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_performUnaryUpdate(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = performUnaryUpdate_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "performUnaryUpdate failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["performBinaryInsert"] = Processor.process_performBinaryInsert
    self._processMap["performBinaryDelete"] = Processor.process_performBinaryDelete
    self._processMap["performBinaryUpdate"] = Processor.process_performBinaryUpdate
    self._processMap["performUnaryInsert"] = Processor.process_performUnaryInsert
    self._processMap["performUnaryDelete"] = Processor.process_performUnaryDelete
    self._processMap["performUnaryUpdate"] = Processor.process_performUnaryUpdate

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_performBinaryInsert(self, seqid, iprot, oprot):
    args = performBinaryInsert_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performBinaryInsert_result()
    result.success = self._handler.performBinaryInsert(args.relationName, args.column1, args.column2)
    oprot.writeMessageBegin("performBinaryInsert", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_performBinaryDelete(self, seqid, iprot, oprot):
    args = performBinaryDelete_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performBinaryDelete_result()
    result.success = self._handler.performBinaryDelete(args.relationName, args.column1, args.column2)
    oprot.writeMessageBegin("performBinaryDelete", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_performBinaryUpdate(self, seqid, iprot, oprot):
    args = performBinaryUpdate_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performBinaryUpdate_result()
    result.success = self._handler.performBinaryUpdate(args.relationName, args.old_column1, args.old_column2, args.new_column1, args.new_column2)
    oprot.writeMessageBegin("performBinaryUpdate", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_performUnaryInsert(self, seqid, iprot, oprot):
    args = performUnaryInsert_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performUnaryInsert_result()
    result.success = self._handler.performUnaryInsert(args.relationName, args.column1)
    oprot.writeMessageBegin("performUnaryInsert", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_performUnaryDelete(self, seqid, iprot, oprot):
    args = performUnaryDelete_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performUnaryDelete_result()
    result.success = self._handler.performUnaryDelete(args.relationName, args.column1)
    oprot.writeMessageBegin("performUnaryDelete", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_performUnaryUpdate(self, seqid, iprot, oprot):
    args = performUnaryUpdate_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = performUnaryUpdate_result()
    result.success = self._handler.performUnaryUpdate(args.relationName, args.column1)
    oprot.writeMessageBegin("performUnaryUpdate", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class performBinaryInsert_args:
  """
  Attributes:
   - relationName
   - column1
   - column2
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'column1', None, None, ), # 2
    (3, TType.STRING, 'column2', None, None, ), # 3
  )

  def __init__(self, relationName=None, column1=None, column2=None,):
    self.relationName = relationName
    self.column1 = column1
    self.column2 = column2

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.column2 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryInsert_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.column1 is not None:
      oprot.writeFieldBegin('column1', TType.STRING, 2)
      oprot.writeString(self.column1)
      oprot.writeFieldEnd()
    if self.column2 is not None:
      oprot.writeFieldBegin('column2', TType.STRING, 3)
      oprot.writeString(self.column2)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performBinaryInsert_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryInsert_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performBinaryDelete_args:
  """
  Attributes:
   - relationName
   - column1
   - column2
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'column1', None, None, ), # 2
    (3, TType.STRING, 'column2', None, None, ), # 3
  )

  def __init__(self, relationName=None, column1=None, column2=None,):
    self.relationName = relationName
    self.column1 = column1
    self.column2 = column2

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.column2 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryDelete_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.column1 is not None:
      oprot.writeFieldBegin('column1', TType.STRING, 2)
      oprot.writeString(self.column1)
      oprot.writeFieldEnd()
    if self.column2 is not None:
      oprot.writeFieldBegin('column2', TType.STRING, 3)
      oprot.writeString(self.column2)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performBinaryDelete_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryDelete_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performBinaryUpdate_args:
  """
  Attributes:
   - relationName
   - old_column1
   - old_column2
   - new_column1
   - new_column2
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'old_column1', None, None, ), # 2
    (3, TType.STRING, 'old_column2', None, None, ), # 3
    (4, TType.STRING, 'new_column1', None, None, ), # 4
    (5, TType.STRING, 'new_column2', None, None, ), # 5
  )

  def __init__(self, relationName=None, old_column1=None, old_column2=None, new_column1=None, new_column2=None,):
    self.relationName = relationName
    self.old_column1 = old_column1
    self.old_column2 = old_column2
    self.new_column1 = new_column1
    self.new_column2 = new_column2

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.old_column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.old_column2 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.new_column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.new_column2 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryUpdate_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.old_column1 is not None:
      oprot.writeFieldBegin('old_column1', TType.STRING, 2)
      oprot.writeString(self.old_column1)
      oprot.writeFieldEnd()
    if self.old_column2 is not None:
      oprot.writeFieldBegin('old_column2', TType.STRING, 3)
      oprot.writeString(self.old_column2)
      oprot.writeFieldEnd()
    if self.new_column1 is not None:
      oprot.writeFieldBegin('new_column1', TType.STRING, 4)
      oprot.writeString(self.new_column1)
      oprot.writeFieldEnd()
    if self.new_column2 is not None:
      oprot.writeFieldBegin('new_column2', TType.STRING, 5)
      oprot.writeString(self.new_column2)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performBinaryUpdate_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performBinaryUpdate_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryInsert_args:
  """
  Attributes:
   - relationName
   - column1
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'column1', None, None, ), # 2
  )

  def __init__(self, relationName=None, column1=None,):
    self.relationName = relationName
    self.column1 = column1

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryInsert_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.column1 is not None:
      oprot.writeFieldBegin('column1', TType.STRING, 2)
      oprot.writeString(self.column1)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryInsert_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryInsert_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryDelete_args:
  """
  Attributes:
   - relationName
   - column1
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'column1', None, None, ), # 2
  )

  def __init__(self, relationName=None, column1=None,):
    self.relationName = relationName
    self.column1 = column1

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryDelete_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.column1 is not None:
      oprot.writeFieldBegin('column1', TType.STRING, 2)
      oprot.writeString(self.column1)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryDelete_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryDelete_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryUpdate_args:
  """
  Attributes:
   - relationName
   - column1
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'relationName', None, None, ), # 1
    (2, TType.STRING, 'column1', None, None, ), # 2
  )

  def __init__(self, relationName=None, column1=None,):
    self.relationName = relationName
    self.column1 = column1

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.relationName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.column1 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryUpdate_args')
    if self.relationName is not None:
      oprot.writeFieldBegin('relationName', TType.STRING, 1)
      oprot.writeString(self.relationName)
      oprot.writeFieldEnd()
    if self.column1 is not None:
      oprot.writeFieldBegin('column1', TType.STRING, 2)
      oprot.writeString(self.column1)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class performUnaryUpdate_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('performUnaryUpdate_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
