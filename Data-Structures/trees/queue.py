class QueueNode:
    def __init__(self,data,nNode=None):
        self.data = data
        self.next = nNode
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def enqueue(self,data):
        new_node = QueueNode(data)
        self.length +=1
        if self.tail is None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise ValueError("Underflow")
        self.length -=1
        retValue = self.head.data
        if self.head.next is None:
            self.head = None
            self.tail = None
            return retValue
        self.head = self.head.next
        return retValue

    def peek(self):
        if self.head is not None:
            return self.head.data
        return None

    def is_empty(self):
        return not self.length >0

    def __len__(self):
        return self.length

    def __str__(self):
        retValue = "Empty queue"
        current = self.head
        if current is not None:
            retValue = "<- "
            while current is not None:
                retValue += str(current.data)+" | "
                current = current.next
            retValue += " <-"
        return retValue
