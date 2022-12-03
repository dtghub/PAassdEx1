a = [38,2,55,98,14,37,63,70,91,55,23,7,63,12,95,9,6,81,25,42,79,5,24,64,12,80,3,9,95,70,72,76,92,89,59,97,36,87,76,49,32,61,42,41,8,78,32,69,31,95]

a = '38'

print(a)

b = {}

if not('frog' in b):
    b['frog'] = []
b['frog'].append(a)

# if 'frog' in b:
#     b['frog'].append(a)
# else:
#     b['frog'] = [a]

print(b)

a = 42

if not('hopper' in b):
    b['hopper'] = {}
# b['hopper'].append(a)

print(b)

if not('tadpole' in b['hopper']):
    b['hopper']['tadpole'] = []
b['hopper']['tadpole'].append(a)

# if 'frog' in b:
#     b['frog'].append(42)
# else:
#     b['frog'] = a

a=456
if not('tadpole' in b['hopper']):
    b['hopper']['tadpole'] = []
b['hopper']['tadpole'].append(a)

invert_index = {}

filename = "myFilename"

set_of_words = {"apple", "banana", "cherry"}

set_of_words2 = {"apple", "banana", "cherry","apple", "banana", "cherry", "orange", "cherry", "pear", "slug"}
list_of_words = ["apple", "banana", "cherry","apple", "banana", "cherry", "orange", "cherry", "pear", "slug","thrush"]


set_to_test = set(list_of_words)
list_to_test = list(set_to_test)
print("\nSet:\n")
print(list_to_test)
print("\n")

total_number_of_words = len(list_of_words)
print("tot wrds:" + str(total_number_of_words))

frequency_of_words = {}
for word in set_of_words2:
    frequency_count = list_of_words.count(word)
    frequency_of_words[word] = frequency_count / total_number_of_words
print("\nFreq:\n")
print(frequency_of_words)
print("\n")

test_embed_in_dict = {}
test_embed_in_dict[filename] = frequency_of_words
filename1 = "myFilename1"
test_embed_in_dict[filename1] = frequency_of_words

print("\nTestFreq:" + str(test_embed_in_dict)+ "\n")

print("\nFileLen:" + str(len(filename))+ "\n")

# invert_index[filename] = []
for word in set_of_words:
    if not(word) in invert_index:
        invert_index[word] = []
    if not(filename) in invert_index[word]:
        invert_index[word].append(filename)

print(invert_index)

filename = "myFilename1"

# invert_index[filename] = []

for word in set_of_words:
    if not(word) in invert_index:
        invert_index[word] = []
    if not(filename) in invert_index[word]:
        invert_index[word].append(filename)


set_of_words = {"apple", "banana", "cherry", "orange", "cherry", "pear", "slug", ""}

for word in set_of_words:
    if not(word) in invert_index:
        invert_index[word] = []
    if not(filename) in invert_index[word]:
        invert_index[word].append(filename)


print("Set of words")
print(set_of_words)
print("\nList of set of words")
print(list(set_of_words))

inv_doc_freq = {}
total_num_docs = len(invert_index)

for word in invert_index:
    doc_count = len(invert_index[word])
    word_index = doc_count / total_num_docs
    inv_doc_freq[word] = word_index
print("\nInvDocFreq")
print(inv_doc_freq)
print("\n")

if not('frog' in b):
    b['frog'] = {}
b['frog'].append(a)




frequency_of_words = {}
for word in list_of_words:
    if word in frequency_of_words:
        frequency_of_words[word] += 1
    else:
        frequency_of_words[word] = 1







    
print("\n")
print(b)
