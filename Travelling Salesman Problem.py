from itertools import permutations

def tsp_bruteforce(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(1, n))
    min_cost = float('inf')

    for path in permutations(cities):
        cost = 0
        current = 0

        for city in path:
            cost += distance_matrix[current][city]
            current = city

        cost += distance_matrix[current][0]
        min_cost = min(min_cost, cost)

    return min_cost


from itertools import combinations

def tsp_held_karp(distance_matrix):
    # DP code here
    pass


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Brute Force:", tsp_bruteforce(distance_matrix))
print("Held-Karp DP:", tsp_held_karp(distance_matrix))