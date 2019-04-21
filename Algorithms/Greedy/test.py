import heapq

def main():
    li = [324,2342,123,234]
    heapq.heapify(li)
    print(li)
    print(heapq.pop(li))

main()