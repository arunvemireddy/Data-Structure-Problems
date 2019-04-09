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
*  O(n^2)
#### Reference
1. [The Coding Train](https://www.youtube.com/watch?v=67k3I2GxTH8) 
---
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
* O(n^2)
#### Reference
1. [My code school](https://www.youtube.com/watch?v=GUDLRan2DWM)
2. [Geeks for Geeks](https://www.youtube.com/watch?v=xWBP4lzkoyM)
---
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
* O(n^2)

#### References:
1. [MIT open course ware](https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3)
2. [My code school](https://www.youtube.com/watch?v=i-SKeOcBwko)
---
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
* (nlogn)
#### References
1. [MIT open course ware](https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3)
2. [Abdul Bari](https://www.youtube.com/watch?v=mB5HXBb_HY8)
---

### 5. Quick Sort
Like merge sort, quick sort is another divide and conqure techinique. Let us take an example to understand Quick Sort. There are N students in the class, and the task for the class it that they have to stand in a line
[  *height wise* ], i.e. shortest person at the front and longest at the back. Just like we used to stand in assembly in our schools. The beauty of the algorithm comes from the same concept, at that times we knew where our place is, so no one had to direct us i.e. sort us. In the same fasion in quick sort the numbers find their own place and don't care about others. Now the question is how do we do that? 

__Steps:__
1. Let the students stand in a line randomly
2. After everyone is in the line mark the first student as PIVOT student (__P__) and LOW (__L__)
3. Put a gigantic student at the end of the line. He is not the part of class, he is just denoting the end of the line. Take a look at the below given animation for the reference. Mark him with a tag HIGH (__H__)
4. Now the __L__ student take a look at his right and tries to find a student with more then __P's__ height and marks him __L__.
5. Simultaneously the __H__ student takes a look at his left and tries to find a student who has lesser height than __P__ and mark him __H__.
6. Once new __H__ and new __L__ are found, they switch places.
7. Go back to step 4, continue doing this untill __H__ is standings left to __L__
8. Onces __H__ is in left of __L__, __P__ swaps places with __H__.
9. Now __P__ is at correct position, everyone in his left are smaller then him (unsorted) and everyone in his right are bigger then him(unsorted).
10. Now imagine everyone on __P's__ left as a new line and everyone on the right another line and continue the whole process again. Simple Recursion

![Alt Text](https://github.com/shubhamg2404/Data-Structure-Problems/blob/master/Media/gif/quick-sort-v1.gif)

#### Pseudocode
Partitation if a function which performs all the tasks which we discussed in above steps

```python
    def partitation(line, low, high):
        p = low                     # Marking P student
        pivote = line[low]         
        l = low, h = high           # Marking L and H students

        while l < h:
            while True:
                l+=1
                if line[l] > pivote:    # Student taller then pivote
                    break
            while True:
                j-=1
                if line[h] <= pivote:   # Student shorted then pivote
                    break
            if l < j:
                swap(line[l], line[h])  #   Change Places
        swap(line[h],line[p])           # Finally pivote at right place
    return h

    def quick_sort(line, low, high):
        if low < high:
            h = partitation(line,low,high)
            quick_sort(line, low, h)
            quick_sort(array, h+1, high)

```

#### Time Complexity
* O(nlogn)

#### Reference
1. [Adbul Bari](https://www.youtube.com/watch?v=7h1s2SojIRw)

---
