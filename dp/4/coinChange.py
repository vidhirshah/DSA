def coinChange(coins:list,amount):
    if amount == 0:
        return 0
    def helper(amount):
        if amount == 0:
            return 0
        mini = 2**31-1
        for i in coins:
            if amount < i:
                continue
            if i == amount:
                return 1
            number = 1 + helper(amount - i)
            mini = min(mini,number)
        return mini
    ans = helper(amount)
    if ans == 2**31-1:
        return -1
    return ans

coins = [2]
amount = 3
print(coinChange(coins,amount))