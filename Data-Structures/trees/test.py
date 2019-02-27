from queue import Queue

def main():
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    print(queue)
main()
