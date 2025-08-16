def knapsack(values, weights, max_weight):
    n = len(values)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for item in range(1, n + 1):
        for weight in range(max_weight + 1):
            if weights[item - 1] <= weight:
                take = values[item - 1] + dp[item - 1][weight - weights[item - 1]]
                skip = dp[item - 1][weight]
                dp[item][weight] = max(take, skip)
            else:
                dp[item][weight] = dp[item - 1][weight]

    # Backtrack to find selected items
    selected = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    print("\n Maximum value that can be carried:", dp[n][max_weight])
    print(" Items selected (0-based index):", selected[::-1])

# === Input Section ===
n = int(input("Enter number of items: "))
values = list(map(int, input("Enter values of items (space-separated): ").split()))
weights = list(map(int, input("Enter weights of items (space-separated): ").split()))
max_weight = int(input("Enter the maximum capacity of the knapsack: "))

# Run the knapsack algorithm
knapsack(values, weights, max_weight)
