import sys

class Edge:
    def __init__(self, source, destination, weight=1):
        # Lets say there is an edge between A -> B
        self.destination = destination      # self.destination will hold B which is the destination from A
        self.source = source                # self.source will hold A as it is the source
        self.weight = weight                # weight between {source}-- (weight) -- > {destination}

    def __str__(self):
        return "{} {}".format(self.destination,self.weight)

class Graph:
    # Constructor 
    # @@Params: optional directions True/False
    def __init__(self,directional=False):
        self.information = {}               # Hashtable for all vertex
        self.directional=directional        # Flag for directional graph

    #method to insert vertex into the graph
    # @@Params: vertex name
    def insert_vertex(self,vertex):
        if vertex not in self.information:      # Add only unique 
            self.information[vertex] = []
    
    # Method to connect to vertex with a weight
    # @@Params: source, destination, weight
    def connect(self,u,v,weight=1):
        if v in self.information and u in self.information:

            self.information[u].append(Edge(u,v,weight))
            if not self.directional:
                self.information[v].append(Edge(v,u,weight))
        else:
            raise ValueError("Vertex not found in Graph")

    #Brute force algorithm to find distance between start and end
    # @@Params: start(source), end(destination)
    def find_distance(self,start,end):

        if start not in self.information or end not in self.information:
            raise ValueError("Vertex not found in graph")

        queue = []
        distance = {}
        for key in self.information:
            distance[key] = -1
        distance[start] = 0
        path = {}
        queue.append(start)
        while len(queue) > 0:
            temp = queue.pop()
            for neighbour in self.information[temp]:
                if distance[neighbour.destination] == -1:
                    distance[neighbour.destination] = distance[temp] + 1
                    path[neighbour.destination] = temp
                    queue.append(neighbour.destination)
        print("path",path)
        print("distance",distance)


    # Implementation of dijkstra's shortest path algorithm
    # @@Params: source, destination
    def dijkstras_shortest_path(self,source,destination):

        if start not in self.information or end not in self.information:
            raise ValueError("Vertex not found in graph")

        distance = {}                   # Distance hashtable
        path = {}                       # Path Hashtable contains the ancestors of a vertex
        for key in self.information:
            distance[key] = sys.maxint
        distance[source] = 0            # Distance from source to source is 0, rest is infinity
        path[source] = source           # Ancestor of source is source
        
        def relax(u,v,w):
            if distance[v] > distance[u] + w:       # If we find the shorter path to the destination
                distance[v] = distance[u] + w       # then change the distance table
                path[v] = u                         # Change the ancestor

        #we will not be needing this if we use Min Priority Queue to extract minimum
        def dequeue(queue,dist):        # Method to find the edge with minimum weight
            min_index = 0
            min = dist[queue[min_index]]
            
            for index,element in enumerate(queue):
                if dist[element] < min:
                    min = dist[element]
                    min_index = index
            return queue.pop(min_index)
                    
        queue = []
        queue.append(source)

        while len(queue) > 0:
            temp = dequeue(queue,distance)                          # Get edge with minimum weight
            for neighbour in self.information[temp]:                # Visit all the neighbours of the edge
                relax(temp,neighbour.destination,neighbour.weight)  # Relax all the neightbours
                queue.append(neighbour.destination)                 # Append the negihtours of current vertex to queue
        
        print("distance",distance)
        print("path",path)

        return distance, path

    # Implementation of bellman-ford shortest path algorithm
    # @@Params: source, destination
    def bellman_ford(self,source,destination):

        if start not in self.information or end not in self.information:
            raise ValueError("Vertex not found in graph")

        all_edges = []      # List containing all edges
        counter = 0         # Counter or number of vertex
        distance = {}       # Distance hashtable
        path = {}           # Path Hashtable contains the ancestors of a vertex
        for vertex in self.information:
            all_edges.extend(self.information[vertex])
            distance[vertex] = sys.maxint
            counter +=1
        distance[source] = 0
        path[source] = source
        
        def relax(u,v,w):
            if distance[v] > distance[u] + w:       # If we find the shorter path to the destination
                distance[v] = distance[u] + w       # then change the distance table
                path[v] = u                         # Change the ancestor

        for i in range(counter-1):                  # For N-1 times where N is the number of vertex
            for edge in all_edges:                  # For all edges in graph
                relax(
                    edge.source,
                    edge.destination,
                    edge.weight)                    # Relax all edges

        print("distance",distance)
        print("path",path)  

    def __str__(self):
        ret_value = ''
        for key in self.information:
            connections = [i.destination for i in self.information[key]]
            ret_value += "'{}': {} \n".format(key,connections)
        return ret_value

# Implementation of Depth First Search
# @@Params: Graph, Empty Directory, Start Node
def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited[node] = True
        for next_node in graph.information[node]:
            dfs(graph,visited,next_node.destination)
    return


# Implementation of Breath First Search
# @@Params: Graph, Empty Directory, Start Node
def bfs(graph,visited,node):
    neighbours = graph.information[node]        # All edges adjecent to the vertex
    queue = neighbours[:]
    print(node)
    visited[node] = True                        # Hashtable to check if the vertex is previously visited
    while len(queue) > 0:
        temp = queue.pop()
        if temp.destination not in visited:     # Check the vertex is previously visited
            visited[temp.destination] = True    # Mark the visited hashtable True
            print(temp)
            queue.extend(graph.information[temp.destination])       # Insert the neighbours of current vertex to queue
    return



def main():
    graph = Graph(directional=True)
    graph.insert_vertex("a")
    graph.insert_vertex("b")
    graph.insert_vertex("c")
    graph.insert_vertex("d")
    graph.insert_vertex("e")
    graph.connect("a","b",4)
    graph.connect("a","c",1)
    graph.connect("c","b",2)
    graph.connect("c","d",4)
    graph.connect("d","e",4)
    graph.connect("b","e",4)
    graph.dijkstras_shortest_path("a","c")
    graph.bellman_ford("a","c")
    
    
    

main()