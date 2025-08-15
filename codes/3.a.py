# Node names for readable output
node_names = {
    0: "Admission Office",
    1: "AB-4",
    2: "Food Court",
    3: "Gym",
    4: "Medical Center",
    5: "Engineering Building",
    6: "Green Garden",
    7: "Central Mosque",
    8: "AB-1",
    9: "Innovation Lab",
    10: "Rowsonara Hall",
    11: "YKSG-2",
    12: "Transport",
    13: "YKSG-1"
}

# Graph edges (u, v, weight)
edges = [
    (0, 1, 3),
    (0, 6, 9),
    (1, 2, 13),
    (2, 3, 5),
    (3, 4, 8),
    (4, 11, -10),
    (11, 5, -3),
    (10, 11, 15),
    (9, 10, 12),
    (8, 9, -2),
    (8, 12, 4),
    (12, 13, 2),
    (6, 7, 6),
    (7, 8, 5)
]

def bellman_ford(edges, num_nodes, start):
    # Step 1: Initialize distances
    dist = [float("inf")] * num_nodes
    dist[start] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break  # No change => optimization

    # Step 3: Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle!")
            return None

    return dist

# Run Bellman-Ford from "Admission Office" (node 0)
start_node = 0
num_nodes = len(node_names)
distances = bellman_ford(edges, num_nodes, start_node)

if distances:
    print(f"Shortest distances from {node_names[start_node]}:\n")
    for node, distance in enumerate(distances):
        if distance == float("inf"):
            print(f"{node_names[start_node]} → {node_names[node]} : No path")
        else:
            print(f"{node_names[start_node]} → {node_names[node]} : {distance}")
