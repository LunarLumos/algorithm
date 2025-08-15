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

# Directed graph adjacency list
graph = {
    0: [1, 6],
    1: [2],
    2: [3],
    3: [4],
    4: [11],
    5: [],
    6: [7],
    7: [8],
    8: [9, 12],
    9: [10],
    10: [11],
    11: [5],
    12: [13],
    13: []
}

# ----------------- Recursive DFS -----------------
def dfs_recursive(node, visited):
    visited.add(node)
    print(node_names[node], end=" → ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)

print("Recursive DFS from Medical Center (Node 4):")
visited_recursive = set()
dfs_recursive(4, visited_recursive)
print("End\n")

# ----------------- Iterative DFS -----------------
def dfs_iterative(start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node_names[node], end=" → ")
            # add neighbors in reverse order to maintain DFS order
            stack.extend(reversed(graph[node]))
    print("End\n")

print("Iterative DFS from Medical Center (Node 4):")
dfs_iterative(4)
