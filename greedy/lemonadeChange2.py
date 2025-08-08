def lemonadeChange(bills):
    cash = [0]*4
    value = [5,10,15,20]
    for i in bills:
        toPay = i - 5
        cash[int(i/5)-1]+=1
        change = 0
        coins = 0
        for i in range(len(cash)-1,-1,-1):
            req = toPay - change
            coins = int(req/value[i])
            if cash[i] >= coins:
                cash[i] -= coins
                change += coins*value[i]
        if change < toPay:
            return False
        print(cash)
    return True

bills = [5,5,5,10,20]
print(lemonadeChange(bills))