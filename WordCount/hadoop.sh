#!/usr/bin/env bash
hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -files mapper.py,reducer.py \
 -input book.txt \
 -output output/ \
 -inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
 -mapper mapper.py \
 -reducer reducer.py