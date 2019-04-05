import sys

class Edge:
    def __init__(self,destination,weight=1):
        #Lets say there is an edge between A -> B
        #self.destination will hold B which is the destination from A
        self.destination = destination
        self.weight = weight
    def __str__(self):
        return "{} {}".format(self.destination,self.weight)

class Graph:
    # Constructor 
    # @@Params: optional directions True/False
    def __init__(self,directional=False):
        self.information = {}
        self.directional=directional

    #method to insert vertex into the graph
    # @@Params: vertex name
    def insert_vertex(self,vertex):
        if vertex not in self.information:
            self.information[vertex] = []
    
    # Method to connect to vertex with a weight
    # @@Params: source, destination, weight
    def connect(self,u,v,weight=1):
        if v in self.information and u in self.information:

            self.information[u].append(Edge(v,weight))
            if not self.directional:
                self.information[v].append(Edge(u,weight))
        else:
            raise ValueError("Vertex not found in Graph")

    #Brute force algorithm to find distance between start and end
    # @@Params: start(source), end(destination)
    def find_distance(self,start,end):
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
        distance = {}
        path = {}
        for key in self.information:
            distance[key] = sys.maxint
        distance[source] = 0
        path[source] = source
        
        def relax(u,v,w):
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                path[v] = u

        #we will not be needing this if we use Min Priority Queue to extract minimum
        def dequeue(queue,dist):
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
            temp = dequeue(queue,distance)
            for neighbour in self.information[temp]:
                relax(temp,neighbour.destination,neighbour.weight)
                queue.append(neighbour.destination)
        print("distance",distance)
        print("path",path)
    
    # Implementation of bellman-ford shortest path algorithm
    # @@Params: source, destination
    def bellman_ford(self,source,destination):
        pass

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
    neighbours = graph.information[node]
    queue = neighbours[:]
    print(node)
    visited[node] = True
    while len(queue) > 0:
        temp = queue.pop()
        if temp.destination not in visited:
            visited[temp.destination] = True
            print(temp)
            queue.extend(graph.information[temp.destination])    
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
    print(graph)
    graph.dijkstras_shortest_path("a","c")
    
    
    

main()