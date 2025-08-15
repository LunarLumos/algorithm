import time
import heapq

# Your graph without negative edge (Lab -> Auditorium removed)
edges = [
    ("Medical_Center", "Library", 5),
    ("Medical_Center", "Cafeteria", 3),
    ("Library", "Dorm_A", 1),
    ("Cafeteria", "Dorm_B", 4),
    ("Dorm_A", "Sports_Complex", 6),
    ("Dorm_B", "Sports_Complex", 5),
    ("Sports_Complex", "Admin_Building", 8),
    ("Admin_Building", "Lab", 2),
    # ("Lab", "Auditorium", -2),  # removed for timing test
    ("Auditorium", "Parking_Lot", 4),
    ("Parking_Lot", "Medical_Center", 10),
    ("Library", "Admin_Building", 9),
]

# Collect all nodes
nodes = set()
for u, v, w in edges:
    nodes.add(u)
    nodes.add(v)

graph = {node: [] for node in nodes}
for u, v, w in edges:
    graph[u].append((v, w))

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    return dist

def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    for _ in range(len(graph) - 1):
        updated = False
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break
    return dist

start_node = "Medical_Center"
runs = 1000

# Time Dijkstra
dijkstra_times = []
for _ in range(runs):
    start_time = time.time()
    dijkstra(graph, start_node)
    dijkstra_times.append(time.time() - start_time)

# Time Bellman-Ford
bellman_times = []
for _ in range(runs):
    start_time = time.time()
    bellman_ford(graph, start_node)
    bellman_times.append(time.time() - start_time)

avg_dijkstra = sum(dijkstra_times) / runs
avg_bellman = sum(bellman_times) / runs

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

print(f"Dijkstra average time over {runs} runs: {GREEN}{avg_dijkstra:.8f} seconds 🚀{RESET}")
print(f"Bellman-Ford average time over {runs} runs: {RED}{avg_bellman:.8f} seconds🐢{RESET}")

if avg_dijkstra < avg_bellman:
    print(f"{YELLOW}Dijkstra is faster ✅ — better for positive-weight graphs!{RESET}")
else:
    print(f"{YELLOW}Bellman-Ford is faster ✅ — unusual, but can happen on small graphs.{RESET}")
