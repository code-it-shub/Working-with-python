from BFS import Graph
from DFS import dfs
from connectedComponents import ConnectedComponents
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
                # self.graph_dict[end]=[start]

        for start,end in edges:
            if end not in self.graph_dict:
                self.graph_dict[end] =[start]
            else:
                self.graph_dict[end].append(start)
                
        print(self.graph_dict)
    def addEdges(self,x,y):
        self.graph_dict[x] =[y]
        self.graph_dict[y] = [x]      
    def Degree(self,key):
        if key in self.graph_dict:
            print(len(self.graph_dict[key]))
        else:
            print("there is no such node with this value")
    def Matrix(self):
        mg=[]
        for i in range(9):
            temp=[]
            for j in range(9):
                temp.append(0)
            mg.append(temp)

        for (v,u) in edges:
            mg[v][u]=1
            mg[u][v]=1
        for items in mg:
            print(items)
        

edges = [
    (5,3),
    (5,7),
    (3,4),
    (3,2),
    (7,8),
    (4,8),
    (6,9)

]
AL=Adjacency(edges)
AL.GraphFormation()
# AL.Matrix()
dfs(AL.graph_dict,5)
print(f"this is number of nodes connected {ConnectedComponents(AL.graph_dict,5)}")
# G=Graph(AL.graph_dict)
# G.bfs(5)