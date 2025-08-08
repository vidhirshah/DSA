def lemonadeChange(bills):
    cash = [0]*3
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
            coins = int(15/10)
            if cash[1] >= coins:
                change += coins*10
                cash[1] -= coins
            coins = int((15 - change)/5)
            if cash[0] >= coins:
                change += coins*10
                cash[0] -= coins
            if change < 15:
                return False
    return True

bills = [5,5,10,10,20]
print(lemonadeChange(bills))