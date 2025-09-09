def coinChange(coins:list,amount):
    dp = []
    for i in range(amount+1):
        dp.append([])
        for j in range(len(coins)):
            dp[i].append(-1)
    def helper(index,amount):
        if amount == 0:
            dp[index][0] = 1
            return 1
        if index == len(coins) -1:
            if amount%coins[index] == 0:
                dp[amount][index] = 1
                return 1
            return 0
        if dp[amount][index] != -1:
            return dp[amount][index]
        take = 0
        if amount >= coins[index]:
            take = helper(index,amount-coins[index])
        nottake = helper(index+1,amount)
        dp[amount][index] = take + nottake
        return take + nottake 
    return helper(0,amount)

coins = [7]
amount = 5
print(coinChange(coins,amount))