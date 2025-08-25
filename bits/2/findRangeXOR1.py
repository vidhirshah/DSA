def findRangeXOR(l,r):
    l -= 1
    xorl = 0
    if l % 4 == 1:
        xorl = 1
    elif l % 4 == 2:
        xorl = l + 1
    elif l % 4 == 3:
        xorl = 0
    else:
        xorl = l
    xorr = 0
    if r % 4 == 1:
        xorr = 1
    elif r % 4 == 2:
        xorr = r + 1
    elif r % 4 == 3:
        xorr = 0
    else:
        xorr = r
    return xorr^xorl

l= 3
r = 5
print(findRangeXOR(l,r))