# Function to sort an array with radix sorting algorithm
# @@Param: list of numbers
def radix_sort(array):
    max_val = max(array)
    max_length = len(str(max_val))
    print(max_length)
    modulo = 10
    ret_value = [[]]*(max_length+1)
    ret_value[0] = array
    print(ret_value)
    for i in range(1,max_length+1):
        for j in range(10):
            for index,value in enumerate(ret_value[i-1]):
                print("here")
                key = value % modulo ** i
                key = key // modulo ** (i-1)     
                if key == j:
                    ret_value[i].append(value)
    return ret_value[max_length]

def main():
    array = [10,16]            
    array = radix_sort(array)
    print(array)
    
main()
