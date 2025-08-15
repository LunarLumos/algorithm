from collections import deque

# Graph adjacency list
graph = {
    'D': ['T', 'P'],
    'T': ['D', 'M', 'K'],
    'M': ['T', 'K', 'B', 'J'],
    'K': ['T', 'M', 'B', 'P'],
    'B': ['M', 'K', 'J', 'G', 'E'],
    'J': ['M', 'B', 'E'],
    'E': ['J', 'B', 'C'],
    'P': ['D', 'K', 'W'],
    'G': ['B', 'W', 'R'],
    'W': ['P', 'G', 'R'],
    'R': ['W', 'G', 'C'],
    'C': ['R', 'E', 'S'],
    'S': ['C']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return traversal_order

# BFS starting from 'M'
start_node = 'M'
order = bfs(graph, start_node)
print("BFS Traversal from", start_node, ":", order)
