# Heaps
A tree with special properties. The basic requirement of heap is that the value of a node must be >= ( or <=) than the value of the root. This is called the heap property. Heap is also an complete binary tree.  

## Operations
* get_parent(x): returns the parent of index x in O(1) time.
* get_left(x): return the index of left child in O(1) time.
* get_right(x): return the index of right child in O(1) time.
* get_max(): returns the max element without deleteing it in O(1) time.
* extract_max(): returns and deletes the max element in O(1) time.
* max_heapify(index): rearranges the heap so that max is on the root in O(logN) time top-down approach.
* perculate_up(index): rearranges the heap so that max is on the root in O(logN) time bottom-top approach.
* insert(element): inserts an element into heap in 0(logN) time.

## Applications
* Priority Queues
* Heap is best data structures to get K largest or k smallest elements
* Priority Queues are used in Dijkstra's Algorithm
* Priority Quees are also used in Prim's Algorithm