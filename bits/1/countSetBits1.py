def countSetBits(n):
    if n == 0:
        return 0
    count = 1
    while n != 1:
        if n & 1 == 1:
            count += 1
        n >>=1
    return count

n = 15
print(countSetBits(n))