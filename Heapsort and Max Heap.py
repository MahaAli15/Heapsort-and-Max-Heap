#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max_heapify(arr,i):
    
    #initialize largest as root
    largest = i
    
    #left = 2 * i + 1
    l = 2 * i + 1
    
    #right = 2 * i + 2
    r = 2 * i + 2
    
    #see if left child of root exists and is greater than root
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    #see if right child of root exists and is greater than root
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    
    #change root,if needed
    if largest != i:
        
        #swap
        arr[i],arr[largest] = arr[largest],arr[i]
        
        #heapify the root
        max_heapify(arr,largest)

#the main function to sort an array of given size
def build_max_heap(arr):
    
    #build a maxheap
    n = int((len(arr) // 2) - 1)
    
    #one by one extract elements
    for i in range(n,-1,-1):
        max_heapify(arr,i)

#driver code
arr = [4,3,7,1,8,5]
build_max_heap(arr)
print(arr)

