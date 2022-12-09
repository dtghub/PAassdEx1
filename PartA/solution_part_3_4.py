from timeit import default_timer as timer
import random


# Although the timings are similar, The Array-based implementation behaves faster, by around 30% on average.

# There is perhaps fewer processing steps involved in moving from one element to the next in the array based version, where it is likely that the starting address of each array element in memory is mostly a calculated value, versus having to retrieve and resolve the pointer to each 'next' element when seeking through the linked list.




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
        

    #search for a given key in the array, returns the (position index + 1) if found, None if not found
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
            
        report = []
        
        
        R = []
        
        for i in range(100):
            R.append(random.randint(0, 49999))


        # time taken to execute is_element(S,x),

        linked_list_ADT = DynamicSet_LinkedList()
        node = NodeDoublyLinkedList
        report.append("Results for Linked-list based implementation")
        
        for list_element in A:
            linked_list_ADT.add(list_element)
        
        for random_element in R:
            start = timer()
            result_of_is_element = linked_list_ADT.is_element(random_element)
            end = timer()
            report.append(str(end - start))
                    

        array_ADT = DynamicSet_Array(20000)
        report.append("Results for Array based implementation")
                
        for list_element in A:
            array_ADT.add(list_element)
    
        for random_element in R:
            start = timer()
            result_of_is_element = array_ADT.is_element(random_element)
            end = timer()
            report.append(str(end - start))
            
 
        link_list_sum = 0
        for i in range(1,101):
            link_list_sum += float(report[i])
       
                
        timing_string = str(link_list_sum/100)
        print("Linked list mean time for 100 searches:", timing_string, "milliseconds")
            
            
        array_sum = 0
        for i in range(102,202):
            array_sum += float(report[i])
        
        timing_string = str(array_sum/100)
        print("Array mean time for 100 searches:", timing_string, "milliseconds")
        
        
        for i in range(len(report)):
            report[i] += "\n"
        
        
        with open('results_problem4.txt', 'w') as f:
            f.writelines(report)
        


class MainEntry:
    def main(self):
        comparison_code = compare_ADT_implementations('int20k.txt')
        comparison_code.main()







test_count = MainEntry()
test_count.main()
