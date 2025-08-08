def minCoins(coins,amount):
    number = 0
    total = 0
    for i in range(len(coins)-1,-1,-1):
        req = amount - total
        used = int(req/coins[i])
        number += used
        total += used*coins[i]
    if total < amount or total > amount:
        return -1
    return number
    
coins = [2,5]
amount = 3
print(minCoins(coins,amount))