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

mutations = [Mutation(column="meta-data:name",value="wangqingshui"), \
            Mutation(column="meta-data:tag",value="pop"), \
            Mutation(column="flags:is_vaild",value="TRUE")]

client.mutateRow(tableName,rowKey,mutations,None)
