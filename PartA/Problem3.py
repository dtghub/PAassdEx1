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



class NodeSinglyLinkedList:
        
    def __init__(self, key = 0):
        self.key = key
        self.nxt = None
    
    
    def get_key(self):
        return (self.key)
    
    def set_key(self, key):
        self.key = key
        
    def get_next(self):
        return (self.nxt)
        
    def set_next(self, nxt):
        self.nxt = nxt
        
        
class SinglyLinkedList:
        
    def __init__(self):
        self.head = None
        print("hello")

        
        
    # checks if linked list is empty
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    #inserts a node object of type NodeSinglyLinkedList at the head of the list
    def insert_head(self, key):
        node = NodeSinglyLinkedList(key)
        node.nxt = self.head
        self.head = node

    #search for a given key in the linked list, returns the node if found, None if not found
    def search_key(self,key):
        node = self.head
        while node != None and node.get_key() != key:
            node = node.get_next()
        return node    

    #returns the number of nodes in the linked list
    def size(self):
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.get_next()
        return (count)

    #iterate through the entire linked list and print all keys
    def print_all_keys(self):
        node = self.head
        while node != None:
            key = node.get_key()
            print(key)
            node = node.get_next()
        
    
list = SinglyLinkedList()
print(list.empty())
list.insert_head(6)
list.insert_head(7)
list.insert_head(61)
list.insert_head(620)
list.insert_head(6)

print("Searching for 6")
foundkey = list.search_key(6)
if foundkey:
    print(foundkey.key)
else:
    print("Not found!")

print("Size: " + str(list.size()))
list.print_all_keys()
print(list.empty())




