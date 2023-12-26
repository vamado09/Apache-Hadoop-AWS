#!/usr/bin/env python3
import sys
import os
import re

def preprocessing(txt):
    txt = txt.lower() # converting to lower case
    txt = re.sub(r'[^\w\s]', ' ', txt) # removing punctuation
    txt = re.sub(r'\b\d+\b', ' ', txt) # removing standalone numbers
    txt = re.sub(r'\s+', ' ', txt).strip() # replacing multiple whitespaces with single space and strip
    return [word for word in txt.split() if word.isalpha()] # tokenizing and retaining only alphabetic words

for line in sys.stdin: # reading line by line
    line = line.strip() # removing whitespaces from input line
    words = preprocessing(line) # clean and tokenize the text

    # Getting the document identifier
    doc_ID = os.path.basename(os.environ["map_input_file"]) # identifer AWS HW8 / GitHub

    for word in words:
        print(f"{word}\t{doc_ID}") # output along document id

# inverted_index_mapper.py: https://gist.github.com/tori-takashi/a5431dde0df603dc260da8d2b35e0ac1
# isalpha(): https://www.geeksforgeeks.org/python-string-isalpha-method/
# regular expressions: https://docs.python.org/3/library/re.html
# regex: https://pynative.com/python-regex-replace-re-sub/
# regex: https://www.geeksforgeeks.org/python-substituting-patterns-in-text-using-regex/