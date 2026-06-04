def generate_subsets(arr):
    n = len(arr)
    subsets = []

    # Iterate through all possible bitmasks
    for mask in range(1 << n):

        current_subset = []

        for i in range(n):

            # Check if i-th bit is set
            if mask & (1 << i):
                current_subset.append(arr[i])

        subsets.append(current_subset)

    return subsets


arr = [1, 2, 3]

result = generate_subsets(arr)

print("All Possible Subsets:")

for subset in result:
    print(subset)