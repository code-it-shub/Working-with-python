def ConnectedComponents(graph,node,visited=set()):
    visited.add(node)
    sm=0
    for child in graph[node]:
        if child not in visited:
            sm=sm+ConnectedComponents(graph,child,visited)
    return sm+1

    