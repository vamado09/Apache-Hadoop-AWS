#!/usr/bin/env python3

import string # punctation
import sys # read and write data to STDIN and STDOUT
import json

# mapper.py to remove punctation and covert words to lowercase (using json file)

for line in sys.stdin:
    txt = json.loads(line) # return json object as dictionary
    review_txt = txt.get("reviewText", "") # get method to get: keyname, value (reviewText comes from json file)
    words = review_txt.split() # split line into words
    
    # Using for loop over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        word = word.strip(string.punctuation).lower() # returns all sets of punctation and lower case
        
        # Output will be the input for the Reduce step (the input for reducer.py)
        if word:
            print ('%s\t%s' % (word, 1)) # results in STDOUT
            
        
# mapper.py
# Source string.punctattion: https://www.geeksforgeeks.org/string-punctuation-in-python/
# Source string.punctation: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
# Source mapper.py: https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/
# Source get() method: https://www.w3schools.com/python/ref_dictionary_get.asp
# Source Json: https://www.geeksforgeeks.org/read-json-file-using-python/