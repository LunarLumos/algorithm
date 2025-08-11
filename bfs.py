def bfs(graph, visited, start, queue):
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

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
target = input("Enter the target node: ")

visited_nodes = []
queue_list = []

print("\nBFS traversal:")
bfs(graph, visited_nodes, source, queue_list)

if target in visited_nodes:
    print(f"\nTarget node '{target}' is reachable from '{source}'.")
else:
    print(f"\nTarget node '{target}' is NOT reachable from '{source}'.")
