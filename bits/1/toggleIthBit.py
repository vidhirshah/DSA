def checkIthBit(n,i):
    temp = 1 << (i-1)
    return n ^ temp

n = 13
i = 1
print(checkIthBit(n,i))