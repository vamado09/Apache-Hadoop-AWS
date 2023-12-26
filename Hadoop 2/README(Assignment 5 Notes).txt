Vicente De Leon
Assignment 5 MAC Terminal Notes

Using Notes from Assignment 4 too*
Assignment 4 sources:
Hadoop Commands: https://sparkbyexamples.com/apache-hadoop/hadoop-hdfs-dfs-commands-and-starting-hdfs-dfs-services/
Hadoop Set Up: https://www.tutorialspoint.com/hadoop/hadoop_enviornment_setup.htm
MapReduce job: https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html
MapReduce job: https://hadoop.apache.org/docs/r1.2.1/streaming.html

HADOOP SERVICES
type: start-all.sh (starting hadoop services)

Task2)
1) After writing Python scripts: mapper_hw5.py and reducer_hw5.py, lets make then available on Desktop:
type: cd ~/Desktop
type: chmod +x mapper_hw5.py (to make the script executable)
type: chmod +x reducer_hw5.py (to make the script executable)
type to check if they exist: ls -l mapper_hw5.py reducer_hw5.py

Adding both datasets into assignment_data HDFS directory just like we did for HW4.
type: hdfs dfs -put data1.csv /assignment_data/
type: hdfs dfs -put data2.csv /assignment_data/
type: hdfs dfs -ls /assignment_data/ (to check if "data1.csv and data2.csv" files are within the HDFS directory)

After seeing that I have a bunch of files and outputs from previous homework I think it's a good idea to clean this up:
type:
hdfs dfs -rm /assignment_data/Kindle_Store_5.json
hdfs dfs -rm -r /assignment_data/output
hdfs dfs -rm -r /assignment_data/output_topN10_Task12
hdfs dfs -rm -r /assignment_data/output_topN10_Task12_combiner
hdfs dfs -rm -r /assignment_data/output_topN_Task12
hdfs dfs -rm -r /assignment_data/output_topN_Task12_combiner
hdfs dfs -rm -r /assignment_data/output_with_combiner_Task12

2)
Hadoop MapReduce job MAC Command:
type:

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files mapper_hw5.py,reducer_hw5.py \
-mapper mapper_hw5.py \
-reducer reducer_hw5.py \
-input /assignment_data/data1.csv \
-input /assignment_data/data2.csv \
-output /assignment_data/output_Task2_hw5


to delete type: hdfs dfs -rm -r /assignment_data/output_Task2_hw5

type to see entire output content: hdfs dfs -ls /assignment_data/output_Task2_hw5

type to see part-00000 content: type: hdfs dfs -cat /assignment_data/output_Task2_hw5/part-00000 (DO NOT RUN!)
type to export data into csv file: hdfs dfs -get /assignment_data/output_Task2_hw5/part-00000 ~/Desktop/output_Task2_hw5.csv
type the following to view heavy csv files using MAC Terminal: head -n 10 ~/Desktop/output_Task2_hw5.csv 



Task3)
My scripts are not working due to the size of the data 673 million lines due to Cartesian Product. I will need to brute force this issue:
type to get 2.0M line file (subset): head -n 2000000 ~/Desktop/output_Task2_hw5.csv > ~/Desktop/smaller_output_Task2_hw5.csv
type the following to view heavy csv files using MAC Terminal (first 10 rows of csv): head -n 10 ~/Desktop/smaller_output_Task2_hw5.csv 

1) Desktop
type: cd ~/Desktop
type: chmod +x sorting_mapper.py (to make the script executable)
type: chmod +x sorting_reducer.py (to make the script executable)
type to check if they exist: ls -l sorting_mapper.py sorting_reducer.py


2)
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files sorting_mapper.py,sorting_reducer.py \
-mapper sorting_mapper.py \
-reducer sorting_reducer.py \
-input /assignment_data/smaller_output_Task2_hw5.csv \
-output /assignment_data/output_Task3_hw5

type the following if you have to delete HDFS output: hdfs dfs -rm -r /assignment_data/output_Task3_hw5

let's display entire content of output directory:
type: hdfs dfs -ls /assignment_data/output_Task3_hw5

type to see part-00000 content: type: hdfs dfs -cat /assignment_data/output_Task3_hw5/part-00000 
type to export data into csv file: hdfs dfs -get /assignment_data/output_Task3_hw5/part-00000 ~/Desktop/output_Task3_hw5.csv
type the following to view heavy csv files using MAC Terminal: head -n 10 ~/Desktop/output_Task3_hw5.csv 

Comparing file line counts:
checking file size (has to match 2 million lines): wc -l ~/Desktop/smaller_output_Task2_hw5.csv
checking file size (has to match 2 million lines): wc -l ~/Desktop/output_Task3_hw5.csv

END: stop-all.sh

Task 4)
Creating subsets:
cd ~/Desktop
type: head -n 200 ~/Desktop/data1.csv > ~/Desktop/smaller_data1.csv  
type: head -n 200 ~/Desktop/data2.csv > ~/Desktop/smaller_data2.csv
type: head -n 40000 ~/Desktop/output_Task2_hw5.csv > ~/Desktop/40k_join_results.csv

After having complete scripts for Task 4 please run (on Desktop):
type: cd ~/Desktop
type: python3 unitesting.py

OR

type: python3 -m unittest unitesting.py
