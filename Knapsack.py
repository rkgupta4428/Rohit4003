def knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    max_profit = 0

    for mask in range(1 << n):
        total_weight = 0
        total_value = 0

        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_value += values[i]

        if total_weight <= capacity:
            max_profit = max(max_profit, total_value)

    return max_profit


def knapsack_dp(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Brute Force:", knapsack_bruteforce(weights, values, capacity))
print("Dynamic Programming:", knapsack_dp(weights, values, capacity))