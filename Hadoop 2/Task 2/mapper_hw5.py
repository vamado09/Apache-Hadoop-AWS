#!/usr/bin/env python3

import sys

for line in sys.stdin: # reading line by line
    line = line.strip() # removing whitespaces from input line
    cols = line.split(",") # splitting line using comma (data is comma_separated)
    
    # Some Python logic based on datasets columns Stack Overflow source
    if len(cols) == 6: # data1 has 6 columns we need VICTIMIZATION_PRIMARY
        key = cols[1] # VICTIMIZATION_PRIMARY Data1
        value = "data1.csv," + ",".join(cols) # value from data1 + columns joined into a single string using ","
    else:
        key = cols[4] # VICTIMIZATION_PRIMARY Data2
        value = "data2.csv," + ",".join(cols) # value from data2 + columns joined into a single string using ","
        
    print(key + "\t" + value)
    
# Using join to concatenate the elements of a list into single string (using "," delimeter). "cols" is our list of columns extracted from the input line.
# mapper_hw5.py will read each data from both datasets. For each, it will output the VICTIMIZATION_PRIMARY as the key and the rest of the data as value 
# along with for dataset identification.
        
    
# Mapreduce join tutorial: https://blog.matthewrathbone.com/2016/02/09/python-tutorial.html
# Mapreduce join tutorial: https://medium.com/@aw.shubh/join-algorithm-using-map-reduce-941f3437b483
# mapper.py base hw4 : https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
# StackOverflow: https://stackoverflow.com/questions/25720178/input-split-for-map-function-in-hadoop
# using join: https://www.mygreatlearning.com/blog/join-in-python/#:~:text=In%20Python%2C%20the%20join(),specified%20string%20as%20a%20separator.