def checkIthBit(n,i):
    temp = 1 << (i-1)
    return n | temp

n = 9
i = 2
print(checkIthBit(n,i))