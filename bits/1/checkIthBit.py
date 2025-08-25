def checkIthBit(n,i):
    for counter in range(i-1):
        n  >>= 1
    if n%2:
        return True
    return False

n = 13
i = 4
print(checkIthBit(n,i))