#!/usr/bin/env bash
rm -fR "./macierze/output/mmj"

hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files macierze/"mmj_mapper.py",macierze/"mmj_reducer.py" \
-output macierze/output/mmj/ \
-input macierze/macierzM.txt \
-inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
-mapper macierze/"mmj_mapper.py" \
-reducer macierze/"mmj_reducer.py" \

