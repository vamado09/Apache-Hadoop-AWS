#!/usr/bin/env python3

import sys

for line in sys.stdin: # reading line by line
    # date -> first value, full_line -> remaining line value
    date, full_line = line.strip().split("\t", 1) # removing white spaces and splitting input line in two parts as before based on tab
    part = full_line.split("\t") # splitting full_line into parts using tab
    if len(part) == 2:  # just making sure the above code was properly split into two main parts
        dataset1, dataset2 = part # extracting dataset
        print(dataset1 + "\t" + dataset2)


       


