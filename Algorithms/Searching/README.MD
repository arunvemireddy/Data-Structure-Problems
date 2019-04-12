# Searching
An algorithm to find data

### Types of Searching
* Unordered Linear Search
* Sorted/Ordered Linear Search
* Binary Search
* Interpolation search
* Symbol Tables and Hashing
* String Searching Algorithms Tries, Tenrary Search and Suffix Trees

### 1. Unordered Linear Search

```python
    for each element in array:
        if element == key:
            print("found" element)
            break
    else:                               # this else will be called if break statement is not called
        print("Not found")
```
#### Time Complexity
* O(N) searching for the whole array in worst case

### 2. Ordered Linear Search
```python
    for each element in array:
        if element == key:
            print("found" element)
            break
        elif element > key:
            print("not found")
            break
```
#### Time Complexity
* O(N) searching for the whole array in worst case

### 3. Binary Search
Binary search is performed on a sorted array. Let us take an example of line of students standing in an assembly line, and the task is we have to find the student with height 175 cm. Below are give heights of students.
__[100, 105, 108, 116, 124, 130, 138, 140, 147, 160, 175, 179, 185]__
Now if i want to find the student with height 175cm one thing which we can do is visit this first student in the line, as that student what is his height. If his height is 175 cm we have found our student, otherwise repeat this process until the last student. A better way of doing this would be as we already know how many student there are in the class. Go to the middle student and his for his height, lets call this student __M__. if __M__'s height is less than 175 cm we don't want to look to his left, and if his height greater than 175 then we want to look to his left.
```
                                M
[100, 105, 108, 116, 124, 130, 138, 140, 147, 160, 175, 179, 185]
```
as  __M__'s height is less than 175 we still have 6 students remaining.

Think of this as a new line of students as there are 6 students there can be two mid lets take 160 as a new mid student
```
            M
[140, 147, 160, 175, 179, 185]
```
Again 160 is less than 175 so we do not want to look to __M__'s left we have 3 students left

```
       M
[175, 179, 185]
```
As 179 is greater than 175 dont look at __M__'s right, and we are left with only one student.
```
  M
[175]
```
Finally we go to new __M__ as ask for his height, and finally we got out student.

See how we were reducing the number of students in searching space, as we are cutting exactly half of our students in each iteration time complexity of this algorithm is O(logN)

#### pseudocode

```python
    def binary_search(array,key):
        length = len(array)                     # First find the length of the array/students
        if length ==1:                          # Check if only one element is in the list
            return array[0] == key              # Return true if key == one element, return false otherwise
        mid = len(array)//2                     # Find the mid of the list
        if array[mid]==key:                     # If mid element is the key return true
            return True
        elif key < array[mid]:                      # If key is less than mid element
            return binary_search(array[:mid],key)   # Do binary search on 0 to mid-1 element
        else:
            return binary_search(array[mid:],key)   # Else do a binary search on mid+1 to last element
```

#### Time Complexity
1. [My code school](https://www.youtube.com/watch?v=j5uXyPJ0Pew)
2. [Abdul Bari](https://www.youtube.com/watch?v=uEUXGcc2VXM)