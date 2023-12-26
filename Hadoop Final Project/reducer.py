#!/usr/bin/env python3

import sys

# initializing variables -> current word and set to store doc IDs
current_word = None
current_docs = set()

for line in sys.stdin: # reading line by line
    line = line.strip() # removing whitespaces from input line
    word, doc_ID = line.split("\t", 1) # splitting line into word and its doc ID

    if current_word == word: # if current word == word in the line
        current_docs.add(doc_ID) # then add doc ID to the set
    else:
        if current_word is not None:  # if word has changed and if current_word is not None -> output the current word and its doc ID
            print(f"{current_word}\t{','.join(sorted(current_docs))}")  # Output -> comma-separated list
        current_word = word
        current_docs = {doc_ID}  # starting a new set of document IDs for the new word

# After preprocessing, return the last word and its doc IDs if it exists
if current_word is not None:
    print(f"{current_word}\t{','.join(sorted(current_docs))}")  # Output -> comma-separated list


# add(): https://www.geeksforgeeks.org/set-add-python/
# join: https://www.geeksforgeeks.org/python-string-join-method/
# sorted: https://www.geeksforgeeks.org/python-sorted-function/