from random import randrange

class MaxHeap:
    def __init__(self):
        self.array = [ 51, 88, 73 , 63 ,65 , 78, 108]
        self.count  = 0
    def find_parent(index):
        if index < 0 or index > len(self.array):
            return -1
        return (index-1)//2
    def get_left(self,index):
        left = (index*2+1)
        if left > len(self.array)-1:
            return -1
        return left
    def get_right(self,index):
        right = index*2+2
        if right > len(self.array)-1:
            return -1
        return right
    def get_max(self):
        if self.count ==0:
            return -1 
        return self.array[0]
    
    def max_heapify(self,index):
        if index < 0 or index > len(self.array)-1:
            return
        left = self.get_left(index)
        right = self.get_right(index)
        max_index = index
        if left != -1 and self.array[left] > self.array[max_index]:
            max_index = left
        if right != -1 and self.array[right] > self.array[max_index]:
            max_index = right
        if max_index != index:
            self.array[index], self.array[max_index] = self.array[max_index], self.array[index]
            self.max_heapify(max_index)
    
    def construct(self):
        self.array.append(14)
        self.array.append(15)
        self.array.append(13)

    def build_max_heap(self,array):
        self.array = array
        middle = len(array)//2
        for i in range(middle,-1,-1):
            self.max_heapify(i)
        return
    def extract_max(self):
        length = len(self.array)
        if(length==0):
            return -1
        length -=1
        self.array[0],self.array[length] = self.array[length],self.array[0]
        retValue = self.array.pop()
        self.max_heapify(0)
        return retValue

    def __str__(self):
        return str(self.array)
    def __len__(self):
        return len(self.array)


def heap_sort(array):
    heap = MaxHeap()
    heap.build_max_heap(array)

    length = len(heap)
    retValue = []
    for i in range(length):
        max_value = heap.extract_max()
        retValue.append(max_value)
    return retValue


def main():
   
    array = []
    for i in range(10):
        array.append(randrange(10,100))
    print(array)
    print(heap_sort(array))
main()


         
