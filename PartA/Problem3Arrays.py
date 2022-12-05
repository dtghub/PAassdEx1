# Problem 3 [10 marks]
# The Dynamic Set is an abstract data type (ADT) that can store distinct elements, without any
# particular order. As opposed to static or frozen sets, dynamic sets allow insertion and deletion
# of elements. That is, they are mutable. There are five main operations in the ADT:
# •
# •
# •
# •
# •
# add(S,x): add element x to S, if it is not present already
# remove(S,x): remove element x from S, if it is present
# is_element(S,x): check whether element x is in set S
# set_empty(S): check whether set S has no elements
# set_size(S): return the number of elements of set S
# Implement in Python1 the Dynamic Set ADT defined above using
# a) A doubly linked list.
# b) A static array implementation (size of array may be picked arbitrarily)



        
class DynamicSet_Array:
        
    def __init__(self):
        self.max_array_list_size = 100
        self.array_list = [None]*self.max_array_list_size
        self.array_list_size = 0
        print("hello")



    #add an element at the end, if the key doesn't already exist. Return position index of key, or None if add operation failed.
    def add(self, key):
        
        key_position = self.is_element(key)
        if key_position == None and self.array_list_size < self.max_array_list_size:
            
            self.array_list[self.array_list_size] = key
            key_position = self.array_list_size
            self.array_list_size += 1

        return key_position
               
        
    
    #use is_element to find key to remove. Return removed position index, or None if not found
    def remove(self, key):
        key_position = self.is_element(key)
        if key_position != None:
            self.array_list = self.array_list[:key_position] + self.array_list[key_position + 1:]
            self.array_list_size -= 1
        return key_position
        

    #search for a given key in the array, returns the position index if found, None if not found
    def is_element(self, key):
        key_found = None
        i = 0
        while i < self.array_list_size and key_found == None:
            if self.array_list[i] == key:
                key_found = i
            i += 1
            
        return key_found    
    
    
    # checks if array is empty
    def set_empty(self):
        if self.array_list_size == 0:
            return True
        else:
            return False


    #returns the number of elements in the array
    def set_size(self):
        return (self.array_list_size)


    #iterate through the entire linked list and print all keys
    def print_all_keys(self):
        for i in range(self.array_list_size):
            print(self.array_list[i])
        



    
list = ArrayList()
print(list.set_empty())
print('Adding 6:' + str(list.add(6)))
print('Adding 7:' + str(list.add(7)))
print('Adding 61:' + str(list.add(61)))
print('Adding 620:' + str(list.add(620)))
print('Adding 6:' + str(list.add(6)))

print("Searching for 6")
foundkey = list.is_element(6)
if foundkey != None:
    print(foundkey)
else:
    print("Not found!")
    
print("Searching for 8")
foundkey = list.is_element(8)
if foundkey != None:
    print(foundkey)
else:
    print("Not found!")

print("Size: " + str(list.set_size()))
list.print_all_keys()
print(list.set_empty())




