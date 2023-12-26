#!/usr/bin/env python3

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin: # read entire line from STDIN
    line = line.strip() # remove white spaces 
    word, count = line.split('\t', 1) # splitting the data on the basis of tab we have provided in mapper.py
    count = int(count) # convert count (currently a string) to int
    
    # The IF-switch only works because Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count)) 
        current_count = count
        current_word = word
        
if current_word == word: # don't forget to output the last word if needed*
    print('%s\t%s' % (current_word, current_count))
    
    

# Source Reducer.py: https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/