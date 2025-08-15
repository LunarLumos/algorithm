import heapq

def dijkstra_with_paths(graph, start):
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent

def build_path(parent, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    return path[::-1]

def print_paths_and_distances(graph, graph_name, expected_dist=None):
    print(f"\nResults for {graph_name}:")
    dist, parent = dijkstra_with_paths(graph, 'A')
    for node in sorted(graph.keys()):
        path = build_path(parent, node)
        if dist[node] == float('inf'):
            print(f"Node {node} is unreachable")
        else:
            print(f"Path to {node}: {' → '.join(path)} | Distance: {dist[node]}")
            if expected_dist and node in expected_dist and dist[node] != expected_dist[node]:
                print(f"  ⚠️ ERROR: Distance {dist[node]} differs from expected {expected_dist[node]} (Dijkstra fails with negatives)")

# Define graphs
graph_positive = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

graph_negative = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', -5), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

# Expected distances for negative graph (correct result)
expected_negative_dist = {
    'A': 0,
    'B': 2,
    'C': -3,
    'D': 0,
}

print_paths_and_distances(graph_positive, "Positive Graph (Non-negative weights)")
print_paths_and_distances(graph_negative, "Negative Graph (Contains negative weight)", expected_negative_dist)
