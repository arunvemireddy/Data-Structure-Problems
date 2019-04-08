# Function to sort an array with insertion sorting algorithm
# @@Param: list of numbers
def quick_sort(array,low,high):
    if low < high:
        j = partiation(array,low,high)
        quick_sort(array,low,j)
        quick_sort(array,j+1,high)


# Function to place the pivote at the right place
# @@Param: array, low, high
def partiation(array,low,high):
    pivote = array[low]
    i,j = low,high

    while i < j:
        while  True:
            i+=1
            if array[i] > pivote:
                break

        while True:
            j-=1
            if array[j] <= pivote:
                break
        if i < j:
            print("swaping: I:{} J:{}".format(i,j))
            array[i],array[j] = array[j],array[i]
        
    array[j],array[low] = array[low],array[j] 
    return j

def main():
    array = [10,16,8,12,15,6,3,9,5,1000]            # note that 1000 is playing the role of infinity
    quick_sort(array,0,len(array)-1)
    print(array)
    
main()
