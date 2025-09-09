def coinChange(coins:list,amount):
    if amount == 0:
        return 1
    dp = [0]*(amount+1)
    dp[0] = 1
    for coin in coins:
        # print(coin)
        for i in range(coin,amount+1):
            if i == coin:
                dp[i] += 1
            else:
                dp[i] =dp[i]+dp[i-coin]
            # print(dp)
    return dp[amount]

coins = [7]
amount = 0
print(coinChange(coins,amount))