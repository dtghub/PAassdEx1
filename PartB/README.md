# The PA Directory Search Engine

## What to write here
You should present the following complexity analysis in this report:

+ Big-O complexity of the indexing operation.
+ Big-O complexity of a search operation (given that indexing has been done already).
+ Big-O complexity of a search operation if it were implemented in a brute force fashion (that is, no indexing performed, all search queries go through the entire text of all files every time).

You should be very clear about what you mean by n when presenting your Big-O complexity analysis.

## The Report


Big-O complexity of the indexing operation.

Each document is indexed from crawl_folder(), using a for loop (O(n))
    The for loop calls index_file() for each file

index_file() starts with some O(1) operations, before reaching the first for loop (O(n)
    which calls parse_line, which is O(n) based on number of lines in the array

    from looking up the functions involved, inv_doc_freq is worst case O(n)

    The for loop calculating the size of the file is O(n) based on number of lines.

    doc_rank[filename] = 1 / total_doc_len has a worst case lookup of O(n), but there are only 13 documents

    total_number_of_words = len(list_of_words) is worst case O(n) based on number of words

    for word in list_of_words: (for loop O(n))

    for word in freq_count_dict: (for loop O(n))

    for word in set_of_words: (for loop O(n))


    Based on the above, the BigO will be O(n) based on the number of words in a document

    The bubble sort is O(n**2) where n is the number of documents being sorted (max 13 documenst = 169




    Big-O complexity of a search operation (given that indexing has been done already).


    for search_word in search_words: is O(n) based on the number of search terms
        within this for loop document_list.intersection(search_word_doc_list) would in worst case be O(n) based on n=13 (number of documents) or number of search terms.

    for doc in document_list:
        for search_word in search_words: this nested loop will be O(n**2), but in practice, the 2 values for n would be number of documents and number of search words - many thousands of words - i.e. vastly greater time to search the words than for searcjhing the indexes











    Big-O complexity of a search operation if it were implemented in a brute force fashion (that is, no indexing performed, all search queries go through the entire text of all files every time).

    In this situation, with optimal codeing, it would be O(n) of the sum of the number of words in each document searched





...
