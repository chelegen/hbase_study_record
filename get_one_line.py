from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('master',9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
transport.open()

tableName = 'new_music_table'
rowKey = '1100'

result = client.getRow(tableName,rowKey,None)

for r in result:
    print 'the row is ',r.row
    print 'the name is ',r.columns.get('meta-data:name').value
    print 'the flag is ',r.columns.get('flags:is_vaild').value
