"""This program implements linear search algorithms having a time complexity of O[n]. 
   It compares every element of the array to the key.
"""

def linear_search(array, key):
    len_array = len(array)
    t = None
    for i in range(len_array):
        if array[i] == key:
            t = i
        else:
            pass
    if t != None:
        print("Found {} at position {} in the array.".format(key, t))
    else:
        print("{} not present in the array.".format(key))
        
array = list(map(int, input("Enter elements of array separated by space: ").split()))
key = input("Enter element to find: ")
linear_search(array, key)
