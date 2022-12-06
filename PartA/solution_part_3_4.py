from timeit import default_timer as timer
import random


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




class NodeDoublyLinkedList:
        
    def __init__(self, key = 0):
        self.key = key
        self.prv = None
        self.nxt = None
    
    
    def get_key(self):
        return (self.key)
    
    def set_key(self, key):
        self.key = key
        
    def get_next(self):
        return (self.nxt)
        
    def set_next(self, nxt):
        self.nxt = nxt
        
    def get_prev(self):
        return (self.prv)
        
    def set_prev(self, prv):
        self.prv = prv
        
# This is the ADT - shoul;d rename it as such        
class DynamicSet_LinkedList:
        
    def __init__(self):
        self.head = None



    #add (insert) a node object at the head, if the key doesn't already exist.Return new node, or None if already exists
    def add(self, key):
        node = None
        isAlreadyExists = self.is_element(key)
        if not(isAlreadyExists):
            node = NodeDoublyLinkedList(key)
            
            if self.set_empty():
                node.set_next(None)
            else:
                node.set_next(self.head)
                self.head.set_prev(node)
                
            node.set_prev(None)
            self.head = node    
        return node
            
        
    
    #use is_element to find node to remove. Return removed node, or None if not found
    def remove(self, key):
        node = self.is_element(key)
        if node:
            nextNode = node.get_next()
            prevNode = node.get_prev()
            if nextNode:
                nextNode.set_prev(prevNode)
            if prevNode:
                prevNode.set_next(nextNode)
            else:
                self.head = nextNode
        return node
        

    #search for a given key in the linked list, returns the node if found, None if not found
    def is_element(self,key):
        node = self.head
        while node and node.get_key() != key:
            node = node.get_next()
        return node
    
    
    # checks if linked list is empty
    def set_empty(self):
        if self.head == None:
            return True
        else:
            return False


    #returns the number of nodes in the linked list
    def set_size(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.get_next()
        return count


    #iterate through the entire linked list and print all keys
    def print_all_keys(self):
        node = self.head
        while node:
            key = node.get_key()
            print(key)
            node = node.get_next()
        





class DynamicSet_Array:
        
    def __init__(self, array_size):
        self.max_array_list_size = array_size
        self.array_list = [None]*self.max_array_list_size
        self.array_list_size = 0



    #add an element at the end, if the key doesn't already exist. Return position index of key, or None if add operation failed.
    def add(self, key):
        
        key_position = self.is_element(key)
        if key_position == None and self.array_list_size < self.max_array_list_size:
            self.array_list[self.array_list_size] = key
            key_position = self.array_list_size
            self.array_list_size += 1

        return key_position != None
               
        
    
    #use is_element to find key to remove. Return removed position index, or None if not found
    def remove(self, key):
        key_position = self.is_element(key)
        if key_position != None:
            key_position -= 1
            self.array_list = self.array_list[:key_position] + self.array_list[key_position + 1:]
            self.array_list_size -= 1
        return key_position != None
        

    #search for a given key in the array, returns the position index + 1 if found, None if not found
    def is_element(self, key):
        key_found = None
        i = 0
        while i < self.array_list_size and key_found == None:
            if self.array_list[i] == key:
                key_found = i + 1
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
        




class compare_ADT_implementations:
    
    def __init__(self, file):
        self.file = file
    
    
    def main(self):
        
        with open(self.file, 'r', encoding="utf-8") as f:
            
            input_file = f.readlines()
        
        
        A = []
        for line in input_file:
            A.append(int(line))
            
        # S = set(A)
        
        
        R = []
        
        for i in range(100):
            R.append(random.randint(0, 49999))


        linked_list_ADT = DynamicSet_LinkedList()
        
        for list_element in A:
            linked_list_ADT.add(list_element)
        
        
        
        
        list_start = 0
        list_end = len(A) - 1
        
        start = timer()
        
        # algo(A, list_start, list_end)
        
        end = timer()
        
        return end - start


class MainEntry:
    def main(self):
        print("You have reached the 'main()' function, please leave a message after the tone...")

        comparison_code = compare_ADT_implementations('int20k.txt')
        result = comparison_code.main()



    def __init__(self):
        print("Howdy!!!")
        # self.main()




test_count = MainEntry()
test_count.main()

# list = DoublyLinkedList()
# print(list.set_empty())
# print('Adding 6:' + str(list.add(6).get_key()))
# print('Adding 7:' + str(list.add(7).get_key()))
# print('Adding 61:' + str(list.add(61).get_key()))
# print('Adding 620:' + str(list.add(620).get_key()))
# print('Adding 6:' + str(list.add(6)))

# print("Searching for 6")
# foundkey = list.is_element(6)
# if foundkey:
#     print(foundkey.key)
# else:
#     print("Not found!")
    
# print("Searching for 8")
# foundkey = list.is_element(8)
# if foundkey:
#     print(foundkey.key)
# else:
#     print("Not found!")

# print("Size: " + str(list.set_size()))
# list.print_all_keys()
# print(list.set_empty())




