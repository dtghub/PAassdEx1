"""
Practical Algorithms, 2021
Assessed Exercise 1
Tester script for all parts
The module names, functions names and their arguments must be compatible
with this tester (i.e., you should make sure you program to this API)
"""

import time
import random as rand
import sys

#%%===========================================================================
#            TESTING PART 1
#=============================================================================

print("*******************************************************************")
print(f"                TESTING PART 1 and 2")
print("*******************************************************************")

#%% TestSortingAlgorithms
#======================
def TestSortingAlgorithms(SortAlgoToTest):
    """ This version does not presume to have any library SORT function
    to use as golden reference. 
    It compares each element to test if the ascending order is maintained
    
    Parameters
    ----------
    SortAlgoToTest : Sorting Algorithm to test. Algorithm should accept
                     just three parameters:
                         1. the unsorted array.
                         2. the starting index of range to be sorted (p)
                         3. the ending index of range to be sorted (r)
                                 
    Returns
    -------
    None.
    
    """
    N = 10     # size of input array
    K = 1000   # range of numbers in input array
    
    #these two arguments that are passed to the sorting algos 
    # mark the starting and ending index of the range
    #to be sorted. we always want to sort the entire array 
    p = 0
    r = N-1 
    
    print("===================================================================")
    print(f"This is a test for USER sort Function :: {SortAlgoToTest.__name__}")
    print("===================================================================")
    print(f"Creating random list of {N} integers in the range 1 - {K}")
    print("")
    
    #random array
    a_unsorted = rand.sample(range(1,K),N)
    
    #fixed array, for debug:
    #a_unsorted =  [35, 24, 824, 332, 546, 31, 429, 945, 654, 646]

    print(f"Unsorted list is :\n", a_unsorted)
    print("")    
       
    #Testing InsertionSort (1a) functionality
    print(f"Testing USER sort function...")    
    a_sorted_testing = a_unsorted.copy()
    try:
        SortAlgoToTest(a_sorted_testing, p, r)
    except:
        print(f"\nERROR: Testing not carried out. "
              f"Unable to execute the required function {SortAlgoToTest.__name__} OR "
              f"function has runtime errors"
              )    
    
    #test result 
    passed = 1
    for i in range (1,N):
        if a_sorted_testing[i] <  a_sorted_testing[i-1]:
            passed = 0
            print("TEST FAILED!")
            print(f"This is the output that failed :\n", a_sorted_testing)
            print("")
            break
    
    if passed:        
        print("TEST PASSED")
        print(f"Sorted list is :\n", a_sorted_testing)
        print("")    

#%% Testing solution to part 1
# Your solution must have the correct API for the following test to be 
# done successfully        

import solution_part_1_2 as sol12

#QUICKSORT test
TestSortingAlgorithms(sol12.QUICKSORT)

#BUBBLESORT test
TestSortingAlgorithms(sol12.BUBBLESORT)

#INSERTIONSORT test
TestSortingAlgorithms(sol12.INSERTIONSORT)

#MERGESORT test
TestSortingAlgorithms(sol12.MERGESORT)



#%%===========================================================================
#            TESTING PART 2
#=============================================================================
# 1. QUICKSORT
# 2. BUBBLESORT
# 3. INSERTIONSORT
# 4. MERGESORT
# using a function called TimeSortingAlgo(SortAlgoToTime,FileIn)
# All these functions should be available in the module "solution_part1"

def TestMultipleSortingAlgos(algos,file):
    """
    Convenience function for testing multiple sorting algos against given file
    Presumes this timing function is defined in the solution
      "sol12.TimeSortingAlgo"

    Parameters
    ----------
    algos : name of algorithms to be tested in a list
          : Each sorting algo should have this interface
          :   ALGOTOSORT(ARRAY, STARTING_INDEX, STOPPING_INDEX)
    file : text file containing elements to be sorted (integers, one per line)

    Returns
    -------
    None.

    """
    
    print ("")
    print(f"Time taken to sort {file}:")
    for algo2sort in algos:
        t = sol12.TimeSortingAlgo(algo2sort,file)
        print(f"{algo2sort.__name__:14} : {t} milliseconds")
    print ("")

print("===================================================================")
print(f"Timing 4 Sorting Algorithms on variety of input sizes")
print("===================================================================")

algos = [ sol12.QUICKSORT
        , sol12.BUBBLESORT
        , sol12.INSERTIONSORT
        , sol12.MERGESORT
        ]

TestMultipleSortingAlgos(algos, "int10.txt")
TestMultipleSortingAlgos(algos, "int50.txt")
TestMultipleSortingAlgos(algos, "int100.txt")
TestMultipleSortingAlgos(algos, "int1000.txt")
TestMultipleSortingAlgos(algos, "int1000_presorted_ascending.txt")
TestMultipleSortingAlgos(algos, "int1000_presorted_descending.txt")


#%%===========================================================================
#   PART 3
#=============================================================================
import solution_part_3_4 as sol34

#%% Test  DynamicSet_LinkedList
print("*******************************************************************")
print(f"                      TESTING PART 3")
print("*******************************************************************")

  
# testing LinkedList-based Implementation
#----------------------------------------
dsll =  sol34.DynamicSet_LinkedList()

dsll.add(1)
dsll.add(3)
dsll.add(5)
dsll.add(1)
dsll.set_empty()

try:
    assert (not dsll.set_empty() == True)
    assert (dsll.set_size() == 3)
    assert (dsll.is_element(3))
    assert (dsll.is_element(5))
    assert (dsll.is_element(1))
    assert (not dsll.is_element(8))
    
    dsll.remove(5)
    dsll.remove(3)
    dsll.remove(3)
    dsll.remove(1)
    assert (not dsll.is_element(3))
    assert (dsll.set_empty())
    assert (dsll.set_size()==0)
    print (f"LinkedList Implementation of Dyanmic Set ADT... PASS")
except AssertionError:
    print (f"LinkedList Implementation of Dyanmic Set ADT... FAIL")
    


# testing Array based Implementation
#-----------------------------------
dsa =  sol34.DynamicSet_Array(10)

dsa.add(1)
dsa.add(3)
dsa.add(5)
dsa.add(1)
dsa.set_empty()

try:
    assert (not dsa.set_empty() == True)
    assert (dsa.set_size() == 3)
    assert (dsa.is_element(3))
    assert (dsa.is_element(5))
    assert (dsa.is_element(1))
    assert (not dsa.is_element(8))
    
    dsa.remove(5)
    dsa.remove(3)
    dsa.remove(3)
    dsa.remove(1)
    assert (not dsa.is_element(3))
    assert (dsa.set_empty())
    assert (dsa.set_size()==0)
    print (f"Array-based Implementation of Dyanmic Set ADT... PASS")
except AssertionError:
    print (f"Array-based Implementation of Dyanmic Set ADT... FAIL")
    
