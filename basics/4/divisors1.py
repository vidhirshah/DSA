def divisors(x):
    result = [x]
    for i in range(1,int(x/2) + 1):
        if x % i == 0:
            result.append(i)
    return sorted(result)

print(60,divisors(60))
print(36,divisors(36))
print(100,divisors(100))
print(162,divisors(162))
print(729,divisors(729))