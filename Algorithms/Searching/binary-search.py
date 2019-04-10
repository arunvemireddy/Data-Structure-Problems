# Function to in a element in array
# @@Params array and key
def binary_search(array,key):
    length = len(array)
    if length ==1:
        return array[0] == key
    mid = len(array)//2
    if array[mid]==key:
        return True
    elif key < array[mid]:
        return binary_search(array[:mid],key)
    else:
        return binary_search(array[mid:],key)

def main():
    array = [1,2,3,4,5,6]
    answer = binary_search(array,10)
    print(answer)

main()