from stack import Stack

#Creating a Stack Data Structure with Queue
class QueueWithStack:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self,data):
        self.first_stack.push(data)

    def dequeue(self):
        if not self.second_stack.is_empty():
            return self.second_stack.pop().data
        else:
            if self.first_stack.is_empty():
                raise ValueError("UnderFlow")
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop().data)
            return self.second_stack.pop().data

def main():
    queue = QueueWithStack()
    for i in range(1,10):
        queue.enqueue(i)
    for i in range(1,10):
        print ( queue.dequeue () )
main()
