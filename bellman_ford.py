def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    n = len(graph)

    for _ in range(n - 1):
        updated = False
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True
        if not updated:
            break

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Negative weight cycle detected")

    return distances

graph = {
    '1': [('2', 10), ('3', 3), ('4', 4)],
    '2': [('1', 2), ('3', 5), ('4', 6)],
    '3': [('1', 7), ('2', 7), ('4', 1)],
    '4': []
}

start_node = '1'
distances = bellman_ford(graph, start_node)

for node, dist in distances.items():
    print(f"Distance from {start_node} to {node} is {dist}")
