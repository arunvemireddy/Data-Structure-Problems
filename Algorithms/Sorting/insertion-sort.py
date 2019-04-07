# Function to sort an array with insertion sorting algorithm
# @@Param: list of numbers
def insertion_sort(array):
    for key in range(1,len(array)):
        current = array[key]
        iterator = key
        while array[key-1] > current and iterator >=1:          # Do swapping while previous element
            array[iterator] = array[iterator-1]                 # is greated then current element
            iterator -=1
        array[iterator] = current 

                

def main():
    array = [100,90,80,70]
    insertion_sort(array)
    print(array)
    
main()
