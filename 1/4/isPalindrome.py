def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    t1 = x
    ans = 0
    while t1!=0:
        ans = ans * 10 + t1 % 10
        t1 = int(t1 / 10)
    if ans == x:
        return True
    return False

print(isPalindrome(12310))