def activity_bruteforce(start, finish):
    n = len(start)
    best = 0

    for mask in range(1 << n):

        activities = []

        for i in range(n):
            if mask & (1 << i):
                activities.append((start[i], finish[i]))

        activities.sort(key=lambda x: x[0])

        valid = True

        for i in range(1, len(activities)):
            if activities[i][0] < activities[i - 1][1]:
                valid = False
                break

        if valid:
            best = max(best, len(activities))

    return best


def activity_greedy(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    count = 1
    last_finish = activities[0][1]

    for s, f in activities[1:]:

        if s >= last_finish:
            count += 1
            last_finish = f

    return count


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print("Brute Force:", activity_bruteforce(start, finish))
print("Greedy:", activity_greedy(start, finish))