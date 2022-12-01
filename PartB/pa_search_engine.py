# -*- coding: utf-8 -*-

"""
Module: 
pa2022_search_engine

About:
Implements functions used by a directory search engine

SOME FUNCTIONS OR THEIR SKELETONS HAVE BEEN PROVIDED
HOWEVER, YOU ARE FREE TO MAKE ANY CHANGES YOU WANT IN THIS FILE
AS LONG AS IT REMAINS COMPATIBLE WITH main.py and tester.py
"""

#%% ---------------------------------------------------------------------------
# Required Imports
#------------------------------------------------------------------------------
import string
from timeit import default_timer as timer
import os

#%%----------------------------------------------------------------------------
def dict_to_file(di, fi):
    with open(fi, "w") as f:
        for key, value in di.items():
            f.write("%s:%s\n" % (key, value))

#%%----------------------------------------------------------------------------
def print_result(result):
    """
    Print result (all docs with non-zero weights)
    """
    print("# Search Results:")
    count = 0
    for val in result: 
        if val[1] > 0: 
            print(val[0])
            count += 1
    print(count, " results returned")

#%%----------------------------------------------------------------------------
def crawl_folder(folder
                ,forward_index
                ,invert_index
                ,term_freq
                ,inv_doc_freq
                ,doc_rank
                ):
    """"
    Crawls a given folder, and runs the indexer on each file
    """
    
    total_docs = 0
    for file in os.scandir(folder):
        if file.is_file():
            total_docs += 1
            index_file(file.name, file.path, forward_index, invert_index, term_freq, doc_rank)

    # with invert_index calculated, we can calculate the inv_doc_freq of each unique word
    # where inv_doc_freq = number of documents with the word / total number of documents
    for word in invert_index.keys():
        inv_doc_freq[word] = len(invert_index[word])/total_docs
        
#%%----------------------------------------------------------------------------
def sanitize_word(word):
    """
    Removes all non ascii characters from a given word
    """    
    newword = ""
    word_len = len(word)
    
    for i in range(word_len):
        char_to_check = word[i]
        char_num = ord(char_to_check)
        if char_num > 96 and char_num < 123:
            newword += char_to_check
            
    return(newword)

#%%----------------------------------------------------------------------------
def parse_line(line):
    """    
    Parses a given line, 
    removes whitespaces, splits into list of sanitize words
    Uses sanitize_word()
    
    HINT: Consider using the "strip()" and "split()" function here
    
    """    
    
    list_of_words = []
    split_up_line = line.split()
    
    for word_to_add in split_up_line:
        # these methods could be chained into one line, but I've left them separate for code readability/maintainability - check timings and briefly mention in report
        lowercase_word = word_to_add.lower()
        # stripped_word = word_to_add.strip() check if this step improves the timing?
        sanitised_word = sanitize_word(lowercase_word)
        list_of_words.append(sanitised_word)
    
    return(list_of_words)

#%%----------------------------------------------------------------------------
def index_file  (filename
                ,filepath
                ,forward_index
                ,invert_index
                ,term_freq
                ,doc_rank
                ):
    """    
    Given a file, indexes it by calculating its:
        forward_index
        term_freq
        doc_rank
    and updates the global invert_index
    """
    start = timer()
    with open(filepath, 'r', encoding="utf-8") as f:
    
    # <YOUR-CODE-HERE>      

        # create a list and a set of words from the text file
        file_content = f.readlines()
        list_of_words = parse_line(file_content)
        set_of_words = set(list_of_words)
        
        # add the set of unique words to forward_index
        forward_index[filename] = list(set_of_words)
        
        # create an entry in term_freq
        # make a dict of key:values for word:frequency_count
        frequency_of_words = {}
        for word in set_of_words:
            frequency_count = list_of_words.count(word)
            frequency_of_words[word] = frequency_count
            
        # store this new dict in the term_freq dict
        term_freq[filename] = frequency_of_words
    
    
    
    
    
    
    
    
    
        
    
    end = timer()
    print("Time taken to index file: ", filename, " = ", end-start)

#%%----------------------------------------------------------------------------
def search  (search_phrase
             ,forward_index
             ,invert_index
             ,term_freq
             ,inv_doc_freq
             ,doc_rank    
             ):
    """    
    For every document, you can take the product of TF and IDF 
    for term of the query, and calculate their cumulative product. 
    Then you multiply this value with that documents document-rank 
    to arrive at a final weight for a given query, for every document. 
    """
    
    words = parse_line(search_phrase)
    result = {}

    <YOUR-CODE-HERE>           

    return(sorted_result)
