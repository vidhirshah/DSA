def checkIthBit(n,i):
    temp = 1 << (i-1)
    temp = ~temp
    return n & temp

n = 13
i = 2
print(checkIthBit(n,i))