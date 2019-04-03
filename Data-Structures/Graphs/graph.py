class Edge:
    def __init__(self,destination,weight=1):
        self.destination = destination
        self.weight = weight
    def __str__(self):
        return "{} {}".format(self.destination,self.weight)
class Graph:
    def __init__(self,directional=False):
        self.information = {}
        self.directional=directional
    def insert_vertex(self,vertex):
        if vertex not in self.information:
            self.information[vertex] = []
    def connect(self,u,v,weight=1):
        if v in self.information and u in self.information:

            self.information[u].append(Edge(v,weight))
            if not self.directional:
                self.information[v].append(Edge(u,weight))
        else:
            raise ValueError("Vertex not found in Graph")

    def __str__(self):
        ret_value = ''
        for key in self.information:
            retValue += "'{}': {} \n".format(key,self.information[key].__str__())
        return retValue

def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited[node] = True
        for next_node in graph.information[node]:
            dfs(graph,visited,next_node.destination)
    return

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
    graph = Graph()
    graph.insert_vertex("a")
    graph.insert_vertex("b")
    graph.insert_vertex("c")
    graph.insert_vertex("z")
    graph.connect("a","b")
    graph.connect("a","c")
    graph.connect("c","b")
    
    graph.insert_vertex("d")
    graph.insert_vertex("e")
    graph.connect("b","d")
    graph.connect("d","e")
    graph.connect('b','z')
    
    dfs(graph,{},"a")

main()