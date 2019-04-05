from random import randrange

class MaxHeap:
    # Constructor
    # @@Param: unsorted array [optional]
    def __init__(self,array = None):
        self.array = []
        if array is not None and len(array) > 0:
            self.build_max_heap(array)
        self.count  = 0
    
    # Method to find the parent index of a node
    # @@Param: index
    def get_parent(self,index):
        if index < 0 or index > len(self.array):
            return -1
        return (index-1)//2
    
    # Method to find the left child of a node
    # @@Param: node index
    def get_left(self,index):
        left = (index*2+1)
        if left > len(self.array)-1:
            return -1
        return left
    
    # Method to find the right child of a node
    # @@Param: node index
    def get_right(self,index):
        right = index*2+2
        if right > len(self.array)-1:
            return -1
        return right
    # Method to get the max value from the heap without deleting
    def get_max(self):
        if self.count ==0:
            return -1 
        return self.array[0]
    
    # Method to heapify the tree
    # Heapify means root node should have the largest/smallest value
    # @@Param: index
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

    # Method to construct a heap from an array
    # @@Param: array 
    def build_max_heap(self,array):
        self.array = array
        middle = len(array)//2
        for i in range(middle,-1,-1):
            self.max_heapify(i)
        return

    # Method to extract the max value from the heap
    def extract_max(self):
        length = len(self.array)
        if(length==0):
            return -1
        length -=1
        self.array[0],self.array[length] = self.array[length],self.array[0]
        retValue = self.array.pop()
        self.max_heapify(0)
        return retValue

    # Method to insert a node into heap
    # @@Param: new element
    def insert(self,element):
        self.array.append(element)
        self.perculate_up(len(self)-1)
        
    # Method to make the heap right from bottom to top
    # @@Param: index 
    def perculate_up(self,index):
        if(index <= 0):
            return
        parent = self.get_parent(index)
        if self.array[parent] > self.array[index]:
            self.array[parent],self.array[index] = self.array[index],self.array[parent]
            self.perculte_up(parent)


    def __str__(self):
        return str(self.array)
    def __len__(self):
        return len(self.array)

# Function to sort an array with heap sort
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
   
    array = [102,103,105]
    heap = MaxHeap(array)
    heap.insert(1000)
    print(heap)
    
main()


         
