def lemonadeChange(bills):
    cash = [0]*3
    value = [5,10,20]
    for i in bills:
        if i == 5:
            cash[0] += 1
        elif i == 10:
            cash[1] += 1
            if cash[0] > 0:
                cash[0] -= 1 
            else:
                return False
        elif i == 20:
            cash[2] += 1
            change = 0
            coins = 0
            for i in range(len(cash)-1,-1,-1):
                req = 15 - change
                coins = int(req/value[i])
                if cash[i] >= coins:
                    cash[i] -= coins
                    change += coins*value[i]
            if change < 15:
                return False
    return True

bills = [5,5,10,10,20]
print(lemonadeChange(bills))