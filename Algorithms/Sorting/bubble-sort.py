# Function to sort an array with bubble sorting algorithm
# @@Param: list of numbers
def bubble_sort(array):

    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] > array[j]:         # if first element is greater then second element
                array[i], array[j] = array[j], array[i]     # Swap
                

def main():
    array = [100,90,80,70]
    bubble_sort(array)
    print(array)
    
main()    