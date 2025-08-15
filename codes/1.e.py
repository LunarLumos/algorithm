from collections import defaultdict
import itertools
import sys
import time

edges = [
    ("Medical_Center", "Library", 5),
    ("Medical_Center", "Cafeteria", 3),
    ("Library", "Dorm_A", 1),
    ("Cafeteria", "Dorm_B", 4),
    ("Dorm_A", "Sports_Complex", 6),
    ("Dorm_B", "Sports_Complex", 5),
    ("Sports_Complex", "Admin_Building", 8),
    ("Admin_Building", "Lab", 2),
    ("Lab", "Auditorium", -2),
    ("Auditorium", "Parking_Lot", 4),
    ("Parking_Lot", "Medical_Center", 10),
    ("Library", "Admin_Building", 9),
]

graph = defaultdict(list)
for u, v, w in edges:
    graph[u].append((v, w))

tsp_nodes = [
    "Medical_Center",
    "Library",
    "Dorm_A",
    "Sports_Complex",
    "Admin_Building",
    "Lab"
]

def bellman_ford(source):
    dist = {node: float('inf') for node in graph.keys()}
    dist[source] = 0
    for _ in range(len(graph) - 1):
        updated = False
        for u in graph:
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break
    return dist

tsp_dist = {}
for src in tsp_nodes:
    dist_from_src = bellman_ford(src)
    for dst in tsp_nodes:
        tsp_dist[(src, dst)] = 0 if src == dst else dist_from_src.get(dst, float('inf'))

def tsp_bruteforce(locations, dist):
    start = locations[0]
    nodes = locations[1:]
    min_cost = float('inf')
    for perm in itertools.permutations(nodes):
        cost = 0
        current = start
        valid = True
        for nxt in perm:
            step = dist[(current, nxt)]
            if step == float('inf'):
                valid = False
                break
            cost += step
            current = nxt
        if not valid:
            continue
        step = dist[(current, start)]
        if step == float('inf'):
            continue
        cost += step
        if cost < min_cost:
            min_cost = cost
    return min_cost

def tsp_dp(locations, dist):
    n = len(locations)
    all_visited = (1 << n) - 1
    memo = {}

    def visit(city, visited):
        if visited == all_visited:
            return dist[(locations[city], locations[0])]
        if (city, visited) in memo:
            return memo[(city, visited)]
        min_cost = float('inf')
        for nxt in range(n):
            if visited & (1 << nxt) == 0:
                cost = dist[(locations[city], locations[nxt])] + visit(nxt, visited | (1 << nxt))
                if cost < min_cost:
                    min_cost = cost
        memo[(city, visited)] = min_cost
        return min_cost

    return visit(0, 1 << 0)

runs = 10000
bf_total_time = 0
dp_total_time = 0
bf_cost = None
dp_cost = None

for _ in range(runs):
    start = time.time()
    bf_cost = tsp_bruteforce(tsp_nodes, tsp_dist)
    bf_total_time += (time.time() - start)

    start = time.time()
    dp_cost = tsp_dp(tsp_nodes, tsp_dist)
    dp_total_time += (time.time() - start)

bf_avg = bf_total_time / runs
dp_avg = dp_total_time / runs

print(f"[+] Average Brute-force TSP runtime over {runs} runs: {bf_avg:.8f} seconds")
print(f"[+] Average DP-based TSP runtime over {runs} runs: {dp_avg:.8f} seconds")
print(f"[+] Minimum cost found: {bf_cost}")

if dp_avg < bf_avg:
    print(f"✅ DP-based TSP is faster by {bf_avg - dp_avg:.8f} seconds on average.")
else:
    print(f"⚠️ Brute-force TSP is faster by {dp_avg - bf_avg:.8f} seconds (unexpected).")
