def coinChange(coins:list,amount):
    if amount == 0:
        return 0
    dp = [10e9]*(amount+1)
    def helper(amount):
        if amount == 0:
            dp[amount] = 0
            return 0
        INT_MAX = 10e9
        if dp[amount] != 10e9:
            return dp[amount]
        mini = 10e9
        for i in coins:
            if amount < i:
                continue
            if i == amount:
                dp[amount] = 1
                return 1
            number = 1 + helper(amount - i)
            mini = min(mini,number)
        dp[amount] = mini
        return mini
    ans = helper(amount)
    if ans == 10e9:
        return -1
    return ans

coins = [2]
amount = 3
print(coinChange(coins,amount))