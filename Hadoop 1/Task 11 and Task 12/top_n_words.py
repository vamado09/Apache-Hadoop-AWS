#!/usr/bin/env python3

from heapq import nlargest
import sys


# sys.argv are are those values that are passed during calling of program along with the calling statement 
N_value = int(sys.argv[1])  # Getting N value from command in Mac Terminal
word_count = {} # intialize empty dictionary to store word counts

# if you type -> hdfs dfs -ls /assignment_data/output you will see files within the HDFS output directory: SUCESS and part-00000
# We need to focus in part-00000 (results from Task 11 from MapReducing job Word Count)
for line in sys.stdin:
    word, count = line.strip().split("\t") # separting into 2 components: word and count
    word_count[word] = int(count) # convert count (string) into integer
    # the above code also adds key value pair into the dictionary

top_words = nlargest(N_value, word_count, key = word_count.get) # getting the N largest values in the dictionary (Descending order)
print("The top N value pairs are (descending order): ")
for word in top_words: # iterarting over each word in top_words
    print(f"{word}: {word_count[word]}") # word + count


# Sources nlargest: https://www.geeksforgeeks.org/python-n-largest-values-in-dictionary/
# Sources user input: https://www.w3resource.com/python-exercises/python-basic-exercise-10.php
# Source reducer.py word,count: https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
# Source Python Sys documentation: https://docs.python.org/3/library/sys.html
# Source sys.arg: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
# Source sys.argv[0,1,2]: https://www.quora.com/What-does-sys-argv-1-mean-and-how-does-it-work