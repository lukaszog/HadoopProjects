#!/usr/bin/env bash
rm -fR "./macierze/output/mwd"

hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files macierze/"mwd_mapper.py",macierze/"mwd_reducer.py" \
-output macierze/output/mwd/ \
-input macierze/macierz.txt \
-inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
-mapper macierze/"mwd_mapper.py" \
-reducer macierze/"mwd_reducer.py" \

