#!/usr/bin/env bash
rm -fR "./macierze/output/mw"

hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files macierze/"mw_mapper.py",macierze/"mw_reducer.py" \
-output macierze/output/mw/ \
-input macierze/macierz.txt \
-inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
-mapper macierze/"mw_mapper.py" \
-reducer macierze/"mw_reducer.py" \

