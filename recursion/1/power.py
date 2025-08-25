def myPow(x,n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return x
    res = myPow(x,int(abs(n)/2))
    res *= res
    if n%2:
        res *= x
    if n < 0:
        return 1 / res
    return res

x = 2
n = 10
print(myPow(x,n))