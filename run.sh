HADOOP_CMD="/home/master/hadoop-2.6.5/bin/hadoop"
STREAM_JAR_PATH="/home/master/hadoop-2.6.5/share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar"

INPUT_FILE_PATH_1="/input.data_2"
OUTPUT_PATH="/output_hbase"


$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func" \
    -file ./map.py \
    -file "./hbase.tgz" \
    -file "./thrift.tgz"
