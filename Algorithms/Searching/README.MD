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