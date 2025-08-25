def countGoodNumbers(n):
    if n  < 1:
        return 1
    if n % 2:
        return( 5 * countGoodNumbers(n-1))
    else:
        return 4 * countGoodNumbers(n-1)
    return

n = 5
print(countGoodNumbers(n))