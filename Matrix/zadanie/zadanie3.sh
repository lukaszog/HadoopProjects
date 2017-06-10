#!/usr/bin/env bash
rm -fR "./macierze/output/mm"
rm -fR "./macierze/output/mm1"

hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files macierze/"mm1_mapper.py",macierze/"mm1_reducer.py" \
-output macierze/output/mm1/ \
-input macierze/macierzM.txt \
-inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
-mapper macierze/"mm1_mapper.py" \
-reducer macierze/"mm1_reducer.py" \


hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files macierze/"mm2_mapper.py",macierze/"mm2_reducer.py" \
-output macierze/output/mm/ \
-input macierze/output/mm1/part-00000 \
-inputformat org.apache.hadoop.mapred.KeyValueTextInputFormat \
-mapper macierze/"mm2_mapper.py" \
-reducer macierze/"mm2_reducer.py" \

rm -fR "./macierze/output/mm1"
