def noSubStrings(s):
    n = len(s)
    return int((n*(n+1))/2)

s = "aswwdwdq"
print(noSubStrings(s))