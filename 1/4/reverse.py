def reverse(x):
    INT_MIN = -2**31
    INT_MAX = 2**31-1
    ans = 0
    while x!=0:
        if x > 0:
            digit = x % 10
        else:
             digit = x % -10
        x = int(x / 10)
        print(ans)
        if ans > int(INT_MAX / 10) or (ans == int(INT_MAX / 10) and digit > 7):
            return 0
        if ans < int(INT_MIN / 10) or (ans == int(INT_MIN / 10) and digit <  -8):
            return 0
        ans = ans *10 + digit
    return ans
# 2147483647
print(reverse(8463847412))    