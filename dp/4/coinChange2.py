def coinChange(coins:list,amount):
    if amount == 0:
        return 0
    INT_MAX = 10e9
    dp = [10e9]*(amount+1)
    dp[0] = 0
    for i in range(amount+1):
        for coin in coins:
            if i == coin:
                dp[i] = 1
            elif i < coin:
                continue
            else:
                dp[i] = min(dp[i],1+dp[i-coin])
        print(dp)
    if dp[amount] == 10e9:
        return -1
    return dp[amount]

coins = [1,2147483647]
amount = 2
print(coinChange(coins,amount))