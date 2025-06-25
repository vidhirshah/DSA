import math

def divisors(x):
    result = []
    for i in range(1,int(math.sqrt(x))+1):
        if x % i == 0:
            result.append(i)
            result.append(int(x / i))
    return sorted(result)

print(60,divisors(60))
print(36,divisors(36))
print(100,divisors(100))
print(162,divisors(162))
print(729,divisors(729))