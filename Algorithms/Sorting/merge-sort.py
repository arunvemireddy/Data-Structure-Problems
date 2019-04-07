# Function to sort an array with merge sort algorithm
# @@Param: list of numbers
def merge_sort(array):
    if len(array) == 1:
        return array
    left, right = select(array)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
     
# Function to merge two sorted array into single sorted array
# @@Param: two sorted arrays
def merge(left_array,right_array):
    new_array = []
    left, right = 0,0
    while left < len(left_array) and right < len(right_array):
        if left_array[left] < right_array[right]:
            new_array.append(left_array[left])
            left +=1
        else:
            new_array.append(right_array[right])
            right +=1
    if right < len(right_array):
        new_array.extend(right_array[right:])
    if left < len(left_array):
        new_array.extend(left_array[left:])
    
    return new_array

# Function to split an array into two arrays with half the length
# @@Param: array
def select(array):
    mid = len(array)//2
    return array[:mid],array[mid:]

def main():
    array = [100,90,80,70]
    array = merge_sort(array)
    print(array)    
main()
