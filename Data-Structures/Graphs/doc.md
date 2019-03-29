# Graphs
A Graph G is an ordered pair of a set V of vertices and E as edges.
G(V,E)
where V is a set of vertices: {v1,v2,v3,v4,v5}
And E is Edges which can be of two type: ordered or unordered

### Ordered Edges
Ordered Edges are represented by "()" brackets and it means (a,b) != (b,a)
### Unordered Edges
Unordered Edges are represted by "{}" brackets and it means {a,b} == {b,a}

## Types of Graphs
* Directed Graph
* Undirected Graph
* Weighted Graph

## Properties

### Self-Loop
when a vertix have an edge such that E = (x,x). In other words where origin and destinations are same.
### Multi-Edge
More then 1 edges between two vertices. Ex: There can be multiple flights from indore to mumbai.
### Walk
A sequence of vertices where each adjacent pair is connected by an edge. Ex: <A,B,F,H,E,B,A,D> 
### Path
A Walk where no vertices ( thus no edges ) are repeated. Ex: <A,B,F,H>
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

