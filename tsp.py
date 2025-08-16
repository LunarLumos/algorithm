def tsp(graph):
    n = len(graph)
    visited = [False] * n
    min_cost = [float('inf')]
    best_path = [[]]  # To store the path with the minimum cost

    def backtrack(current_city, count, cost_so_far, path):
        if count == n and graph[current_city][0] > 0:
            # Tour complete, return to start
            total_cost = cost_so_far + graph[current_city][0]
            if total_cost < min_cost[0]:
                min_cost[0] = total_cost
                best_path[0] = path + [0]  # complete the tour by returning to city 0
            return

        for next_city in range(n):
            if not visited[next_city] and graph[current_city][next_city] > 0:
                visited[next_city] = True
                backtrack(next_city, count + 1, cost_so_far + graph[current_city][next_city], path + [next_city])
                visited[next_city] = False  # Backtrack

    visited[0] = True  # Start from city 0
    backtrack(0, 1, 0, [0])

    print("Minimum Cost:", min_cost[0])
    print("Minimum Path:", best_path[0])

# Example: 4 cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph)
