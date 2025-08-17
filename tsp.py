import itertools

def tsp_dp(distances):
    n = len(distances)
    memo = {}

    # Initialize base cases
    for i in range(1, n):
        memo[(frozenset([i]), i)] = distances[0][i]

    # Iterate over subset sizes
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            subset = frozenset(subset)
            for city in subset:
                min_cost = float('inf')
                for prev_city in subset:
                    if prev_city == city:
                        continue
                    prev_subset = subset - {city}
                    cost = memo[(prev_subset, prev_city)] + distances[prev_city][city]
                    if cost < min_cost:
                        min_cost = cost
                memo[(subset, city)] = min_cost

    # Compute minimal tour cost
    full_subset = frozenset(range(1, n))
    min_tour_cost = float('inf')
    for last_city in range(1, n):
        cost = memo[(full_subset, last_city)] + distances[last_city][0]
        if cost < min_tour_cost:
            min_tour_cost = cost
            optimal_last_city = last_city

    # Reconstruct path
    path = [0]
    remaining_cities = set(range(1, n))
    current_city = optimal_last_city
    path.append(current_city)
    remaining_cities.remove(current_city)

    while remaining_cities:
        prev_subset = frozenset(remaining_cities)
        min_cost = float('inf')
        next_city = -1
        for city in remaining_cities:
            cost = memo[(prev_subset, city)] + distances[city][current_city]
            if cost < min_cost:
                min_cost = cost
                next_city = city
        path.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    path.append(0)
    path = [path[i] for i in reversed(range(len(path)))]

    return min_tour_cost, path

# Distance matrix
distances = [
    [0, 12, 8, 20, 15],
    [12, 0, 10, 25, 8],
    [8, 10, 0, 14, 12],
    [20, 25, 14, 0, 18],
    [15, 8, 12, 18, 0]
]

min_cost, optimal_path = tsp_dp(distances)
city_names = ["Gulshan", "Dhanmondi", "Badda", "Mirpur", "Mohammadpur"]
optimal_path_names = [city_names[i] for i in optimal_path]

print("Optimal Tour Cost:", min_cost, "km")
print("Optimal Path:", " → ".join(optimal_path_names))
