def divide(dividend, divisor):
    INT_MIN = -2**31
    INT_MAX = 2**31 -1
    ans = 0
    sign = 1
    if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    ans = 0
    while dividend >= divisor:
        temp = divisor
        add = 1
        while dividend -( temp << 1 )> 0:
            temp <<= 1
            add <<= 1
        dividend -= temp 
        ans += add
    ans *= sign
    if ans < INT_MIN:
        return INT_MIN
    if ans > INT_MAX:
        return INT_MAX
    return ans

dividend = -7
divisor = -3
print(divide(dividend,divisor))