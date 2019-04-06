# Graphs
A Graph G is an ordered pair of a set V of vertices and E as edges.
G(V,E)
where V is a set of vertices: {v1,v2,v3,v4,v5}
And E is Edges which can be of two type: ordered or unordered


## Types of Graphs
* Directed Graph
* Undirected Graph
* Weighted Graph

### Ordered Edges
Ordered Edges are represented by "()" brackets and it means (a,b) != (b,a)
### Unordered Edges
Unordered Edges are represted by "{}" brackets and it means {a,b} == {b,a}

## Properties

### Self-Loop
when a vertix have an edge such that E = (x,x). In other words where origin and destinations are same.
### Multi-Edge
More then 1 edges between two vertices. Ex: There can be multiple flights from indore to mumbai.
### Walk
A sequence of vertices where each adjacent pair is connected by an edge. Ex: <A, B, F, H, E, B, A, D> 
### Path
A Walk where no vertices ( thus no edges ) are repeated. Ex: <A, B, F, H>
### Trail
A Walk where vertices can be repeated but edges can't be repeated.

### Strongly/Weakly Connected Graphs
When there is direct connection between all the nodes, ie we can read to any node from any node directly. These kinds or graphs are called Stronly connected graphs, otherwise they are called weakly connected graphs.


## Formulas
* In an directed graph with N verticies there can be N*(N-1) Edges
* Where as in undirected graph there will be (N*(N-1))/2 Edges


## Graph Representation
* Adjacency Matrix
* Adjacency List
* Adjacency Sets

## Applications of Graphs
* Transport Networks: Highways Networks, Flight Networks.
* Computer Networks: LAN, Internet, Web 
* Database: For representing ER Diagrams.


## Breath First Search
BFS is like level order search in Trees. In this first we find all the neighbours of the current node. Once we are finished visiting each neighbours of the current node, we then start to explore the neignbour


#### Reference Links
* [MIT open course ware](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
* [Abdul Bari](https://www.youtube.com/watch?v=pcKY4hjDrxk) 

## Depth First Search 
DFS is similar to DFS of a tree, the only catch in this is that there can be cycles so that we have to take care of cycles. One simple way to do that is to maintain a hashtable to all the nodes which we have visited.

* [MIT open course ware](https://www.youtube.com/watch?v=AfSk24UTFS8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=14)
* [Abdul Bari](https://www.youtube.com/watch?v=pcKY4hjDrxk)

### Edge Classification
* *tree edges:* (Parent Pointer) visite new vertex via edge
* *forward edges:* node to a descendant in a tree
* *bacward edges:* node to an ancestor in a tree
* *cross edges:*  between two subtrees

## Shortest Path Algorithms
__Notations:__
* P is path which is set or verticies. ex <v1,v2,v3>
* W(P): W is a function which calculates the total *work* which is addition of all the weights in the path P. P = [v1,v2,v3] and W = Sum(P)
* Delta(u,v) is a function which finds the total weight to go from u to v, along with the path

### Relaxation
Relaxation is a simple concept with an overly complicated name ( *like all the other things in software engineering* ). The concepts states * "If we find a shorter path to reach the destination just update the weight" *
__sudo code:__
* V: Destination
* U: Source
* W: Weight between U and V
``` python
    if distance[v] > distance[u] + w:       # If we find the shorter path to the destination
        distance[v] = distance[u] + w       # then change the distance table
        path[v] = u                         # Update ancestor
```
### Dijksta's Shortest Path
This algoritm is used to find the shortest paths into DAGs which is directed acyclic graphs. This uses greedy algorithm.


#### Time Complexity
* With Adjacency List and Priority Queue: *O((V+E)logV)*
* With Matrix and Priority Queue: *O(V^2 + ElogV)*
* With FibonacciHeap and Adjacency List: *O(E + VlogV)*

#### Reference Links
* [MIT open course ware](https://www.youtube.com/watch?v=2E7MmKv0Y24&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=16)
* [Abdul Bari](https://www.youtube.com/watch?v=XB4MIexjvY0)

### Bellman-Ford Shortest Path
As we know Dijkstra's shortes path algorithm fails to get us the correct weights if there are negative weights cycle in the graph so we need a better solution.

#### Sudo Code:

```python
    Initilize()
    for i in range(N-1):        # Where N is the number of vertex
        for edge in all_edges_in_graph:
            relax(u, v, w)   #Defination of relaxation given above in the doc
    
    for edge in all_edges_in_graph:         # Check if negative cycles exists
        if distance[v] > distance[u] + w:   # Even after N-1 iterations of relaxations
            There is a Cycle                # If we are able to relax some edges there is a cycle
```

#### Reference Links
* [MIT open course ware](https://www.youtube.com/watch?v=ozsuci5pIso)
* [Abdul Bari](https://www.youtube.com/watch?v=FtN3BYH2Zes)

