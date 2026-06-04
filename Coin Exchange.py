def coin_bruteforce(coins, amount):

    def solve(rem):
        if rem == 0:
            return 0

        if rem < 0:
            return float("inf")

        ans = float("inf")

        for coin in coins:
            ans = min(ans, 1 + solve(rem - coin))

        return ans

    return solve(amount)


def coin_greedy(coins, amount):
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count


def coin_dp(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Brute Force:", coin_bruteforce(coins, amount))
print("Greedy:", coin_greedy(coins, amount))
print("Dynamic Programming:", coin_dp(coins, amount))