# Function to sort an array with selection sorting algorithm
# @@Param: list of numbers
def selection_sort(array):
    key = 0
    min_index = 0
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1,len(array)):
            if (array[i] > array[j]):
                    min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def main():
    array = [100,90,80,70]
    selection_sort(array)
    print(array)
    
main()    