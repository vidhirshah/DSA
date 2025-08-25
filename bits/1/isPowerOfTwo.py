def isPowerOfTwo(n):
    if n == 0:
        return False
    if n & (n-1):
        return False
    return True

n = 0
print(isPowerOfTwo(n))