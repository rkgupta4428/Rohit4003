def brute_force_bin_packing(items, capacity):
    min_bins = [len(items)]

    def solve(index, bins):
        if index == len(items):
            min_bins[0] = min(min_bins[0], len(bins))
            return

        if len(bins) >= min_bins[0]:
            return

        # Try existing bins
        for i in range(len(bins)):
            if bins[i] + items[index] <= capacity:
                bins[i] += items[index]
                solve(index + 1, bins)
                bins[i] -= items[index]

        # Create new bin
        bins.append(items[index])
        solve(index + 1, bins)
        bins.pop()

    solve(0, [])
    return min_bins[0]


items = [4, 8, 1, 4, 2, 1]
capacity = 10

print("Brute Force:")
print("Minimum bins required:", brute_force_bin_packing(items, capacity))

def first_fit_decreasing(items, capacity):
    items = sorted(items, reverse=True)
    bins = []

    for item in items:
        placed = False

        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break

        if not placed:
            bins.append(item)

    return len(bins)


items = [4, 8, 1, 4, 2, 1]
capacity = 10

print("\nFirst Fit Decreasing:")
print("Bins required:", first_fit_decreasing(items, capacity))