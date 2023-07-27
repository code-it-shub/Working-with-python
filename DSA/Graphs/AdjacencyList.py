from BFS import Graph

class Adjacency:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict={}

    def GraphFormation(self):
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]

        for start,end in edges:
            if end not in self.graph_dict:
                self.graph_dict[end] =[]
            else:
                pass
                
        print(self.graph_dict)
    def addEdges(self,x,y):
        self.graph_dict[x] =[y]
        self.graph_dict[y] = [x]      
    def Degree(self,key):
        if key in self.graph_dict:
            print(len(self.graph_dict[key]))
        else:
            print("there is no such node with this value")



edges = [
    (5,3),
    (5,7),
    (3,4),
    (3,2),
    (7,8),
    (4,8)
]
AL=Adjacency(edges)
AL.GraphFormation()

G=Graph(AL.graph_dict)
G.bfs(5)
