def dfs(graph, visited, node):
    visited.append(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, visited, neighbor)

# Build graph from input
graph = {}

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

print("Enter edges (node1 node2) one per line:")

for _ in range(e):
    u, v = input().split()

    # Add u->v
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

    # Add v->u for undirected graph
    if v not in graph:
        graph[v] = []
    graph[v].append(u)

source = input("Enter the source node: ")

visited_nodes = []

print("\nDFS traversal:")
dfs(graph, visited_nodes, source)
