#!/usr/bin/env python3

import sys

current_key = None # current key being processed set to None
data1_rows = [] # empty list to store rows from Data1
data2_rows = [] # empty list to store rows from Data2

for line in sys.stdin: # reading line by line
    line = line.strip() # removing whitespaces from input line
    key, value = line.split("\t", 1) # splitting lines into columns key and value. 1 will allow values to contain tabs
    
    # The following code is kind of tricky:
    # if key is not equal to current key -> it means the program encountered a new key in the input data
    
    if key != current_key: # checking -> new key from input line vs current processed key
        if current_key is not None: # checking that it's not the first key encountered
            for row1 in data1_rows: # iterating through rows from data1 dataset
                for row2 in data2_rows: # iterating through rows from data2 dataset
                    print(row1 + "\t" + row2) # print joined results print(row1 + " " + row2)
                    
        # Let's reset.
        # We need to reset becuase it's the only way the code will be able to handle the next key in the input data without problems.
        # It is important to remember that each key represents a unique group of data records.
        # When key!= current_key (detecting new key), means we are going into a different group of data record with a new key.
        # That's why we need to reset, to prepare for new key.
        current_key = key
        data1_rows = []
        data2_rows = []
    
    dataset, row = value.split(",", 1) # splitting value (seprated by "," in mapper.py) into two parts using ("," and 1) as well -> dataset and row
    # Value format was build with a comma seprating the dataset name and the row data.
    if dataset == "data1.csv": # if dataset equals to dataset 1
        data1_rows.append(row) # if it does, lets append the row to data1_rows list
    elif dataset == "data2.csv": # dataset 2
        data2_rows.append(row) # lets append the row to data2_rows list

# Repeate process
if current_key is not None:
    for row1 in data1_rows:
        for row2 in data2_rows:
            print(row1 + "\t" + row2) # print joined results print(row1 + " " + row2)
            
            
# MapReduce job: https://www.tutorialspoint.com/map_reduce/map_reduce_quick_guide.htm
# Kay Value Pair Hadoop: https://techvidvan.com/tutorials/hadoop-mapreduce-key-value-pair/
# Splitting using split(): https://stackoverflow.com/questions/21462879/in-line-split-1-what-does-the-1-in-the-square-brackets-indicate-in-pytho
# Split(): https://www.geeksforgeeks.org/python-string-split/
# append(): https://www.geeksforgeeks.org/python-list-append-method/
# Using is not None: https://www.w3docs.com/snippets/python/python-if-x-is-not-none-or-if-not-x-is-none.html
