# Sorting
Sorting is an algorithm to arrange number is ascending or descending order.

## Types

### 1. Bubble Sort
The simplest sort there is. Just keep comparing all the numbers in an array and swap them

#### Pseudocode
```python
    array = [10,24,2,5,3,23,5]

    for each i in len(array):                   # Iterate throught whole array as i
        for each j from i to len(array):        # Iterate throught whole array starting from index i
            if(array[i] > array[j]):            # if value at i as more then value at j then swap
                swap(array[i], array[j]) 

```
#### Time Complexity:
* $ O(n^2) $

### 2. Selection Sort
Selection sort is an inplace sorting algorithm which doesnt require any additional space. This works well with files.
And used to sort files which have large values but small keys, as the key are small.

#### Pseudocode

```python
    min = None
    for i in range(len(array)-1):
        min = i
        for j in range(i,len(array)):           # Find the minimum value in the array
            if array[i] > array[j]:             # If smaller number found change min to current
                min = j                         
        swap(array[i],array[j])                 # Swap min with current
```
#### Time Complexity:
* $O(n^2)$

### 3. Insertion Sort

Insertion sort is a simple sorting algorithm which works like we sort the playing cards in our hand.

#### Pseudocode
```python
    for i in range(1,len(arr)):
        current = arr[i]
        j = i
        while previous element is greater then current element:
            swap(previous element, current element)

```

#### Time Complexity
* $O(n^2)$

### 4. Merge Sort
Merge sort is a sorting algorithm which uses divide and conqure method. In merge sort we divide an array into smaller sub arrays and try to sort the smaller sub arrays. After the sub arrays are sorted we merge these sub arrays into big array


#### Pseudocode
Merge sort contains 3 major parts.
1. Spliting of an array into 2 parts
2. Merging two already sorted arrays
3. A recursive function  

```python
    def split(array):                           # array = [1,2,3,4]
        mid = length/2
        left_array = array[0 to mid]            # left_array = [1,2]
        right_array = array[mid to end]         # right_array = [3,4]
        return left_array,right_array
    
    def merge(left_array,right_array):
        new_array = []
        while there are elements in left_array and there are element in right_array:
            if left_element < right_element:
                add left_element to new_array
                increment left_element index
            else:
                add right_element to new_array
                increment right_element index
        
        if there is anthing left in left_array:
            add all the elements of left_array to new_array
        if there is anthing left in right_array:
            add all the elements of right_array to new_array
        
        return new_array
    
    def merge_sort(array):
        if array has one element in it:
            return that element

        left_array, right_array  = split(array)             # split the given array into two  parts
        left_array = merge_sort(left_array)                 
        right_array = merge_sort(right_array)

        return merge(left_array, zright_array)              # finally merge both the sub arrays and return
        
```

#### Time Complexity
* $O(nlogn)$
