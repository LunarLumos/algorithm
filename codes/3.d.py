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

# Directed graph adjacency list with weights (energy cost)
graph = {
    0: [(1, 3), (6, 9)],
    1: [(2, 13)],
    2: [(3, 5)],
    3: [(4, 8)],
    4: [(11, -10)],
    5: [],
    6: [(7, 6)],
    7: [(8, 5)],
    8: [(9, -2), (12, 4)],
    9: [(10, 12)],
    10: [(11, 15)],
    11: [(5, -3)],
    12: [(13, 2)],
    13: []
}

def greedy_dispatch(graph, start, battery):
    """
    Greedy drone dispatch algorithm under limited battery.
    At each step, choose the neighbor with minimum energy cost.
    """
    visited = set()       # Keep track of visited nodes
    current = start       # Start node
    path = [current]      # Path taken
    energy_used = 0       # Total energy consumed

    visited.add(current)
    print(f"Starting dispatch at {node_names[current]} with battery {battery}\n")

    while battery > 0:
        # Find all unvisited neighbors
        neighbors = [(neighbor, weight) for neighbor, weight in graph[current] if neighbor not in visited]
        if not neighbors:
            print("No more reachable nodes or all neighbors visited.")
            break

        # Greedy choice: next node with minimum energy cost
        next_node, cost = min(neighbors, key=lambda x: x[1])

        # Check battery constraint
        if battery - cost < 0:
            print(f"Not enough battery to reach {node_names[next_node]} (cost {cost}). Stopping dispatch.")
            break

        # Update battery and energy used
        battery -= cost
        energy_used += cost

        # Move to next node
        current = next_node
        visited.add(current)
        path.append(current)
        print(f"Moving to {node_names[current]} | Cost: {cost} | Remaining battery: {battery}")

    print("\nDispatch complete!")
    print("Path taken:")
    print(" → ".join(node_names[node] for node in path))
    print(f"Total energy used: {energy_used}")
    print(f"Remaining battery: {battery}\n")


# Example Usage: Drone starts at Admission Office with battery = 20
greedy_dispatch(graph, start=0, battery=20)
