def isarmstrong(x):
    t1 = x
    sum = 0
    while t1 > 0:
        sum = sum + (t1 % 10)**3
        t1 = int(t1 / 10)
    if sum == x:
        return True
    return False

print(isarmstrong(153))