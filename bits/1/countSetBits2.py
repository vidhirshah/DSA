def countSetBits(n):
    if n == 0:
        return 0
    count = 0
    while n > 0:
        n = n & (n-1)
        count += 1
    return count

n = 1
print(countSetBits(n))