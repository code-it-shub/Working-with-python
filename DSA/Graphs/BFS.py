class Graph:
    def __init__(self,graph):
        self.graph = graph
    
    def bfs(self,node):
        visited=[]
        queue=[]
        
        queue.append(node)
        visited.append(node)

        while queue:
            m= queue.pop(0)
            print(m)
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

# graph ={
#     5:[3,7],
#     3:[2,4],
#     7:[8],
#     2:[],
#     4:[8],
#     8:[]

# }

# G= Graph(graph)
# G.bfs(5)