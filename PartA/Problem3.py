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
        
        
class DoublyLinkedList:
        
    def __init__(self):
        self.head = None
        print("hello")



    #add (insert) a node object at the head, if the key doesn't already exist.Return new node, or Null if already exists
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
        
        
        # node = NodeSinglyLinkedList(key)
        # node.nxt = self.head
        # self.head = node
        
        
    
    #use is_element to find node to remove. Return removed node, or Null if not found
    def remove(self, key):
        node = self.is_element(key)
        if node:
            nextNode = node.get_next()
            prevNode = node.get_prev()
            nextNode.set_prev(prevNode)
            prevNode.set_next(nextNode)
        return node
        

    #search for a given key in the linked list, returns the node if found, None if not found
    def is_element(self,key):
        node = self.head
        while node != None and node.get_key() != key:
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
        return (count)


    #iterate through the entire linked list and print all keys
    def print_all_keys(self):
        node = self.head
        while node != None:
            key = node.get_key()
            print(key)
            node = node.get_next()
        



    
list = DoublyLinkedList()
print(list.set_empty())
print('Adding 6:' + str(list.add(6).get_key()))
print('Adding 7:' + str(list.add(7).get_key()))
print('Adding 61:' + str(list.add(61).get_key()))
print('Adding 620:' + str(list.add(620).get_key()))
print('Adding 6:' + str(list.add(6)))

print("Searching for 6")
foundkey = list.is_element(6)
if foundkey:
    print(foundkey.key)
else:
    print("Not found!")
    
print("Searching for 8")
foundkey = list.is_element(8)
if foundkey:
    print(foundkey.key)
else:
    print("Not found!")

print("Size: " + str(list.set_size()))
list.print_all_keys()
print(list.set_empty())




