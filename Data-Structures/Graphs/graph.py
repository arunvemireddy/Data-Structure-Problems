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
        retValue = ''
        for key in self.information:
            retValue += "'{}': {} \n".format(key,self.information[key].__str__())
        return retValue
            
                

def main():
    graph = Graph()
    graph.insert_vertex("a")
    graph.insert_vertex("b")
    graph.insert_vertex("c")
    graph.connect("a","b")
    graph.connect("a","c")
    graph.connect("c","b")

    print(graph)

main()