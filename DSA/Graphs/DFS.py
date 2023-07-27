def dfs(graph,node,visited=set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)


