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
            index_file(file.name, file.path, forward_index, invert_index, term_freq, inv_doc_freq, doc_rank)

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
    split_line = line.split()
    for word_to_add in split_line:
        # these methods could be chained into one line, but I've left them separate for code readability/maintainability - check timings and briefly mention in report
        lowercase_word = word_to_add.lower()
        # print(lowercase_word)
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
                ,inv_doc_freq
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

        # *********************************************
        # NOTE - before adding new documents, check that it doesn't already exist 1st - that way the count of documents stays correct!!!!!!!!
        # *********************************************


        # create a list and a set of words from the text file
        start = timer()
        file_content = f.readlines()
        
        
        list_of_words = []
        for line_to_parse in file_content:
            # split_line = line_to_parse.split()/
            words_from_line = parse_line(line_to_parse)
            # print(words_from_line)
            list_of_words.extend(words_from_line)
        # print(list_of_words)
        
        
        
        
        # list_of_words = parse_line(file_content)
        # print("List of words created: " + str(timer() - start))
        set_of_words = set(list_of_words)
        # print("Set of words created: " + str(timer() - start))
        
        # record the size of the file and record this ad the document rank in doc_rank
        total_doc_len = 0
        for line in file_content:
            total_doc_len += len(line)
        doc_rank[filename] = 1 / total_doc_len
        
        # add the set of unique words to forward_index
        forward_index[filename] = list(set_of_words)
        # print("Forward index created: " + str(timer() - start))
        
        # create an entry in term_freq
        # make a dict of key:values for word:frequency_count
        frequency_count = 1
        total_number_of_words = len(list_of_words)
        frequency_of_words = {}
        freq_count_dict = {}
        for word in list_of_words:
            if word in freq_count_dict:
                freq_count_dict[word] += 1
            else:
                freq_count_dict[word] = 1
            # frequency_count = list_of_words.count(word)
            # print(word + ": frequency_count created: " + str(timer() - start))
        # print(freq_count_dict)
        # print(freq_count_dict['the'])
            
        for word in freq_count_dict:
            frequency_of_words[word] = frequency_count / total_number_of_words
            # print("frequency_of_words[word] created: " + str(timer() - start))
        # print("frequency_of_words created: " + str(timer() - start))
        # store this new dict in the term_freq dict
        term_freq[filename] = frequency_of_words
        # term_freq[filename] = freq_count_dict
        # print("term_freq created: " + str(timer() - start))
        
        # now add the words from set_of_words to invert_index
        for word in set_of_words:
            if not(word) in invert_index:
                invert_index[word] = []
            if not(filename) in invert_index[word]:
                invert_index[word].append(filename)
        
        # print("invert_index created: " + str(timer() - start))
        
        
        # Inverse document frequency (IDF): This is a metric calculated for each unique word encountered, across all documents. It has values between 0 and 1, and is calculated as follows: IDF(word) = Number of documents with word / Total numnber of documents
        
        # use invert_index
        
        total_num_docs = len(invert_index)
        
        for word in invert_index:
            doc_count = len(invert_index[word])
            word_index = doc_count / total_num_docs
            inv_doc_freq[word] = word_index
        
        
        
        
    
    
    
    
    
    
    
    
    
        
    
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
    
    search_words = parse_line(search_phrase)
    
    print(search_words)
    
    result = {}
    result_weightings = {}

    # <YOUR-CODE-HERE>  
#     For every document, you can take the product of TF and IDF for each term of the query, and
# calculate their cumulative product. Then you multiply this value with that documents
# DocumentRank to arrive at a final weight for a given query, for every document. This weight
# is then used to sort your results.
    
    
    
    # take the product of TF and IDF 
    # for term of the query, and calculate their cumulative product
    # spec says need to match all terms, so set to zero if one term is missing
    

    # tf =1
    # idf = 1
    # for search_word in search_words:
    #     if search_word in invert_index:
    #         idf = inv_doc_freq[search_word]
    #         for doc in invert_index[search_word]:
    #             tf = term_freq[doc][search_word]

    #     else:
    #         tf = 0
    # dr = doc_rank[key]
    # result_weighting = tf * idf * dr
    # if result_weighting:
    #     result_weightings[key] = tf * idf * dr
    
    document_list = set(doc_rank)
    # for every document - calculate the document doc_rank
    
    # start by getting list of all docs which have all search terms
    for search_word in search_words:
        if search_word in invert_index:
            search_word_doc_list = set(invert_index[search_word])
            print(search_word_doc_list)
            document_list = document_list.intersection(search_word_doc_list)
            print("Doc list: ")
            print(len(document_list))
            print(document_list)
        else:
            document_list = set()
        
    sorted_result = []
    if len(document_list):
        print("In document_list: ")
        print(len(document_list))
        print(document_list)
        for doc in document_list:
            doc_product = doc_rank[doc]
            for search_word in search_words:
                doc_product *= term_freq[doc][search_word]
                doc_product *= inv_doc_freq[search_word]

            result_weightings[doc_product] = doc
            
        result_order = sorted(result_weightings, reverse=True)
        
        
        for result_weighting in result_order:
            sorted_result.append([result_weightings[result_weighting], result_weighting])
            
                
        
    
    
    
    
    print(sorted_result)
    
    
    # sorted_result = result_weighting
    return(sorted_result)
