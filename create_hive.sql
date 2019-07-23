SET hbase.zookeeper.quorum=master:2181,slave1:2181,slave2:2181;
SET zookeeper.znode.parent=/hbase;
ADD jar /usr/local/src/hive-0.12.0-bin/lib/hive-hbase-handler-0.12.0.jar;

CREATE EXTERNAL TABLE music_table (
    rowkey string,
    meta_data map<STRING,STRING>,
    other_flag map<STRING,STRING>
) STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES ("hbase.columns.mapping" = ":key,meta_data:,other_flag:")
TBLPROPERTIES ("hbase.table.name" = "music_table");
