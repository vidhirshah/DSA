def findRangeXOR(l,r):
    ans = 0
    for i in range(l,r+1):
        ans ^= i
    return ans

l= 3
r = 5
print(findRangeXOR(l,r))