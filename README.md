FOR SEARCHING:
Just copy the searching.py file to your working directory and then import it in the file you are working on.
Import using(for Python):

    from sorting import *

The file is under work but currently has three searching algorithms.
1) Linear Search: The most basic searching algorithm with a time complexity of O(n).
                  This function returns the index of the number to be found and should be used as follows:
                  
                  t = linear_search(array, key)
                  
                  #where array is the list and key is the item to be found.
                 
2) Binary Search: Based on Divide and Conquer algorithm.
                  This function returns the index of the number to be found and should be used as follows:
                  
                  t = binary_search(array, key)
                  
                  #where array is the list and key is the item to be found.

FOR SORTING:
This is one of the most optimized sorting algorithm. The worst case time complexity is O[n*2] but average time complexity is O[nlogn]. The two riveting points of this algorithm are:
1) Randomized selection of pivot element.
2) Three partition method for extremly fast sorting of lists with a lot of similar elements.(a.k.a Dutch National Flag algorithm).


Just copy the sorting.py file to your working directory and then import it in the file you are working on.
Import using(for Python):

    from searching import *
    
To use the algorithms use the following call:
        
        output = quick_sort(list)
        #where list is the list of data.
