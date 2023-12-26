#!/usr/bin/env python3

import sys

for line in sys.stdin: # reading line by line
    part = line.strip().split("\t") # removing white spaces and splitting input line by tab
    if len(part) == 2:  # just making sure the above code was properly split into two main parts
        # Extract date from Dataset 2 and use it as a key for sorting
        date = part[1].split(",")[0] # extracting DATE from dataset 2 and use it as key
        print(date + "\t" + line.strip())
