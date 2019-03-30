class Graph:
    def __init__(self):
        self.information = {}
    def insert_vertex(self,vertex):
        if vertex not in self.information:
            self.information[vertex] = []
    def connect(self,u,v):
        if v in self.information and v in self.information:
            self.information[u].append(v)
            self.information[v].append(u)
        else:
            raise ValueError("Vertex not found in Graph")

    def __str__(self):
        ret_value = ''
        for key in self.information:
            retValue += "'{}': {} \n".format(key,self.information[key].__str__())
        return retValue
    
def construct_visited_nodes(graph):
    ret_value = {}
    for key in graph.information:
        ret_value[key] = False
    return ret_value

def dfs(graph,visited,node):
    if not visited[node]:
        print(node)
        visited[node] = True
        for next_node in graph.information[node]:
            dfs(graph,visited,next_node)
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
    
    visited = construct_visited_nodes(graph)
    dfs(graph,visited,"a")

main()