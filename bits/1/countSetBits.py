def countSetBits(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            count += 1
        n = int(n/2)
    return count

n = 15
print(countSetBits(n))