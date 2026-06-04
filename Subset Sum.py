def subset_sum_bruteforce(arr, target):
    n = len(arr)

    for mask in range(1 << n):

        total = 0

        for i in range(n):
            if mask & (1 << i):
                total += arr[i]

        if total == target:
            return True

    return False


arr = [3, 34, 4, 12, 5, 2]
target = 9

print("Subset Exists:", subset_sum_bruteforce(arr, target))