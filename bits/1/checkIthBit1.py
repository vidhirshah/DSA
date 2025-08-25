def checkIthBit(n,i):
    temp = 1 << (i-1)
    if temp & n:
        return True
    return False

n = 13
i = 2
print(checkIthBit(n,i))