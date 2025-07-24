import math

def isprime(x):
    if x == 1 or x == 2 or x <= 0:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(isprime(131))