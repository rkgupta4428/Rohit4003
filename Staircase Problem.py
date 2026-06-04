def stairs_bruteforce(n):
    if n <= 1:
        return 1

    return stairs_bruteforce(n - 1) + stairs_bruteforce(n - 2)


def stairs_dp(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 5

print("Brute Force:", stairs_bruteforce(n))
print("Dynamic Programming:", stairs_dp(n))