# Graph adjacency list
graph = {
    'M': ['T', 'K', 'B', 'J'],
    'T': ['D', 'K', 'M'],
    'K': ['T', 'M', 'P', 'B'],
    'B': ['M', 'K', 'G', 'J', 'E'],
    'J': ['M', 'B', 'E'],
    'E': ['J', 'B', 'C'],
    'C': ['E', 'R', 'S'],
    'R': ['C', 'G', 'W'],
    'G': ['B', 'R', 'W'],
    'W': ['G', 'R', 'P'],
    'P': ['K', 'W', 'D'],
    'D': ['T', 'P'],
    'S': ['C']
}

# DFS function (recursive)
def dfs(graph, node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)

    return traversal_order

# Perform DFS starting from 'M'
dfs_order = dfs(graph, 'M')
print("DFS Traversal from M:", " → ".join(dfs_order))
