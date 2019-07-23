#!/usr/bin/python
import os
import sys

os.system('tar xvzf hbase.tgz > /dev/null')
os.system('tar xvzf thrift.tgz > /dev/null')

reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("./")

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

def mapper_func():
    for line in sys.stdin:
        ss = line.strip().split('\t')
        if len(ss) != 2:
            continue
        key = ss[0].strip()
        val = ss[1].strip()

        rowKey = key

        mutations = [Mutation(column="meta-data:name",value=val), \
                    Mutation(column="flags:is_vaild",value="TRUE")]
        client.mutateRow(tableName,rowKey,mutations,None)

if __name == "__main__":
    module = sys.modules[__name__]
    func = getattr(module,sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)