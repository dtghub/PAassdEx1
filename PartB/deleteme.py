
def count_unique(list1):
    return(len(set(list1)))

L = [1, 2, 3, 1, 1, 4, 5, 6]
print(count_unique(L))

#%% 4b

import string


def absent_alphabets(string1):
    #reduce string to unique characters
    unique_chars = set(string1.lower())
        
    absentees = []
    
    #check each letter of the alphabet to see if present in the set of 
    #unique characters derived from the input string
    for c in string.ascii_lowercase:
        if(not c in unique_chars):
            absentees.append(c)

    return (absentees)


print(absent_alphabets("A quick brown yes quick brown fox oh that quick brown fox jumps over the lazy cat"))

#%% 4c

def order_neutral_list_comparison(list1, list2):
    return(set(list1) == set(list2))
    
print(order_neutral_list_comparison([1,3,5,7,9], [1,5,7,9,9,3]))

for i in set([1,5,7,9,9,3]):
    
    print(str(i) + " " + str([1,5,7,9,9,3].count(i)))