from queue import Queue

# Function to construct an inter leaving queue
# INPUT 1 2 3 4 5 6
# OUTPUt 1 4 2 5 3 6
# @@Param: queue
def inter_leaving_queue(q):
    if len(q)%2 != 0:
        return
    queues = [Queue(),Queue()]
    length = len(q)
    for i in range(length):
        if(i < int(length/2)):
            queues[0].enqueue(q.dequeue())
        else:
            queues[1].enqueue(q.dequeue())
    new_queue = Queue()  
    for i in range(len(queues[0])):
        new_queue.enqueue(queues[0].dequeue())
        new_queue.enqueue(queues[1].dequeue())
    print(new_queue)

def main():
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    inter_leaving_queue(queue)

main()
