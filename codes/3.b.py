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

# Directed graph edges (u, v, weight)
edges = [
    (0, 1, 3),
    (0, 6, 9),
    (1, 2, 13),
    (2, 3, 5),
    (3, 4, 8),
    (4, 11, -10),
    (11, 5, -3),
    (11, 4, -2),
    (10, 11, 15),
    (9, 10, 12),
    (8, 9, -2),
    (8, 12, 4),
    (12, 13, 2),
    (6, 7, 6),
    (7, 8, 5)
]

def bellman_ford(edges, num_nodes, start):
    dist = [float("inf")] * num_nodes
    parent = [-1] * num_nodes
    dist[start] = 0

    # Relax edges |V| - 1 times
    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("\nGraph contains a negative weight cycle!")

            # Step 1: Find a node in the cycle
            x = v
            for _ in range(num_nodes):
                x = parent[x]

            # Step 2: Trace the cycle
            cycle = []
            curr = x
            while True:
                cycle.append(curr)
                curr = parent[curr]
                if curr == x and len(cycle) > 1:
                    break
            cycle.reverse()
            cycle.append(cycle[0])  # to show loop back

            # Step 3: Calculate total cycle weight
            total_weight = 0
            for i in range(len(cycle)-1):
                for u, v, w in edges:
                    if u == cycle[i] and v == cycle[i+1]:
                        total_weight += w
                        break

            # Step 4: Print cycle with names
            print("Negative Cycle Path:")
            print(" -> ".join(node_names[n] for n in cycle) + f" = {total_weight}")
            return None, None

    return dist, parent

def print_paths(start, dist, parent):
    print(f"\nShortest distances from {node_names[start]}:\n")
    for node in range(len(dist)):
        if dist[node] == float("inf"):
            print(f"{node_names[start]} → {node_names[node]} : No path")
        else:
            path = []
            curr = node
            while curr != -1:
                path.append(node_names[curr])
                curr = parent[curr]
            path.reverse()
            print(f"{node_names[start]} → {node_names[node]} : {dist[node]} | Path: {' -> '.join(path)}")

# Run Bellman-Ford from Admission Office (node 0)
start_node = 0
distances, parent = bellman_ford(edges, len(node_names), start_node)

if distances:
    print_paths(start_node, distances, parent)
