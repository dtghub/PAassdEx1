import sys
from timeit import default_timer as timer
import os

#%%----------------------------------------------------------------------------




def PARTITION(A, start, end):
    x = A[end]
    lrbi = start - 1
    for ti in range(start, end):
        if A[ti] <= x:
            lrbi += 1
            (A[lrbi], A[ti]) = (A[ti], A[lrbi])
    (A[lrbi + 1], A[end]) = (A[end], A[lrbi + 1])
    return lrbi + 1



def QUICKSORT(A, start, end):
    if start < end:
        pivot = PARTITION(A, start, end)
        QUICKSORT(A, start, pivot - 1)
        QUICKSORT(A, pivot + 1, end)


#%%----------------------------------------------------------------------------


def BUBBLESORT(A, start, end):
    for outer in range(end, start, -1):
        for i in range(start, outer):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
        




#%%----------------------------------------------------------------------------

def INSERTIONSORT(A, start, end):
    for outer in range(start + 1, end + 1):
        key = A[outer]
        inner = outer
        while inner > 0 and A[inner - 1] > key:
            A[inner] = A[inner - 1]
            inner -= 1
        A[inner] = key
            

#%%----------------------------------------------------------------------------

def MERGE(A, start, mid, end):
    sys.setrecursionlimit(2000)
    LEFT = A[start:mid]
    RIGHT = A[mid:end]
    
    sentinel = sys.maxsize
    LEFT.append(sentinel)
    RIGHT.append(sentinel)
    
    ti = 0
    li = 0
    ri = 0
    
    for ti in range(start, end):
        if LEFT[li] < RIGHT[ri]:
            A[ti] = LEFT[li]
            li += 1
        else:
            A[ti] = RIGHT[ri]
            ri += 1
        



def MERGESORT(A, start, end):
    # print(A)
    if start < end:
        mid = (start + end) // 2
        MERGESORT(A, start, mid)
        MERGESORT(A, mid + 1, end)
        MERGE(A, start, mid + 1, end + 1)



#%%----------------------------------------------------------------------------

def TimeSortingAlgo(algo, file):
    
    # print(algos)
    
    with open(file, 'r', encoding="utf-8") as f:
        
        input_file = f.readlines()
    
    
    A = []
    for line in input_file:
        A.append(int(line))
    
    list_start = 0
    list_end = len(A) - 1
    
    start = timer()
    
    algo(A, list_start, list_end)
    
    end = timer()
    
    return end - start
    
    
    
    
    


#%%----------------------------------------------------------------------------





a = [38,2,55,98,14,37,63,70,91,55,23,7,63,12,95,9,6,81,25,42,79,5,24,64,12,80,3,9,95,70,72,76,92,89,59,97,36,87,76,49,32,61,42,41,8,78,32,69,31,95]

print(a)
QUICKSORT(a, 0, len(a) - 1)
print(a)
