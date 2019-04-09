# Function to sort an array with counting sorting algorithm
# @@Param: list of numbers
def counting_sort(array):
    max_val = max(array)
    ret_value = []
    auxilary = [0]*(max_val+1)
    for element in array:
        auxilary[element] += 1
    for index,element in enumerate(auxilary):
        if element:
            ret_value.append(index)
    return ret_value
            

def main():
    array = [10,16,8,12,15,6,3,9,5,1000]            
    array = counting_sort(array)
    print(array)
    
main()
