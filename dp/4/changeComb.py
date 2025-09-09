def coinChange(coins:list,amount):
    def helper(index,amount):
        if amount == 0:
            return 1
        if index == len(coins) -1:
            if amount%coins[index] == 0:
                return 1
            return 0
        take = 0
        if amount >= coins[index]:
            take = helper(index,amount-coins[index])
        nottake = helper(index+1,amount)
        return take+ nottake 
    return helper(0,amount)

coins = [1,2,5]

amount = 5
print(coinChange(coins,amount))