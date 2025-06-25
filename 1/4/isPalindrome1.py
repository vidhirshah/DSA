def isPalindrome(x):
    str_x = str(x)
    length = len(str_x)
    for i in range(int(length / 2)):
        if str_x[i] != str_x[length - 1- i]:
            return False
    return True

print(isPalindrome(-1221))