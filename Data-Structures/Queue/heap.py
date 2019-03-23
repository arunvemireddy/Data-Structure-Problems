class Heap:
    def __init__(self,heap_type):
        self.array = []
        self.type = heap_type
        self.count  = 0
    def find_parent(index):
        if index < 0 or index > len(self.array):
            return -1
        return (index-1)/2
    def get_left_child(index):
        left = (index*2+1)
        if left > len(self.array):
            return -1
        return left
    def get_right(index):
        right = index*2+2
        if right > len(self.array):
            return -1
        return right
    def get_max(self):
        if self.count ==0:
            return -1 
        return self.array[0]