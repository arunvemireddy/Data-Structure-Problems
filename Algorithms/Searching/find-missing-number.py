def find_missing_number(first,second):
    ret_value = first[0]
    for i in range(1,len(first)):
        ret_value ^= first[i]
    for element in second:
        ret_value ^= element
    return ret_value

def main():
    first  = [1,2,3,4,5,6]
    second = [1,2,3,4,5]
    missing = find_missing_number(first,second)
    print(missing)

main()