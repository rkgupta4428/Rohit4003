from itertools import permutations

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

max_profit = 0
best_schedule = []

for order in permutations(jobs):
    slots = {}
    profit = 0

    for job in order:
        job_id, deadline, p = job

        for t in range(1, deadline + 1):
            if t not in slots:
                slots[t] = job_id
                profit += p
                break

    if profit > max_profit:
        max_profit = profit
        best_schedule = list(slots.values())

print("===== BRUTE FORCE APPROACH =====")
print("Best Schedule:", best_schedule)
print("Maximum Profit:", max_profit)

jobs_greedy = jobs.copy()
jobs_greedy.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs_greedy)
slots = [None] * (max_deadline + 1)

profit = 0

for job_id, deadline, p in jobs_greedy:
    for slot in range(deadline, 0, -1):
        if slots[slot] is None:
            slots[slot] = job_id
            profit += p
            break

print("\n===== GREEDY APPROACH =====")
print("Scheduled Jobs:", [job for job in slots[1:] if job])
print("Maximum Profit:", profit)

