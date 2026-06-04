def fractional_bruteforce(weights, values, capacity):
    best = 0

    def backtrack(i, remaining, profit):
        nonlocal best

        if i == len(weights):
            best = max(best, profit)
            return

        for fraction in [0, 0.25, 0.5, 0.75, 1]:
            wt = weights[i] * fraction
            val = values[i] * fraction

            if wt <= remaining:
                backtrack(i + 1, remaining - wt, profit + val)

    backtrack(0, capacity, 0)
    return best


def fractional_greedy(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, weight, value in items:

        if capacity >= weight:
            profit += value
            capacity -= weight
        else:
            profit += ratio * capacity
            break

    return profit

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Brute Force:", fractional_bruteforce(weights, values, capacity))
print("Greedy:", fractional_greedy(weights, values, capacity))