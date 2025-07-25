def myAtoi(s):
    INT_MAX = 2**31 -1
    INT_MIN = -2**31
    length = len(s)
    ans = ""
    index = 0
    for i in range(index,length):
        index = i
        if s[i] == " ":
            continue
        elif s[i] == "+" or s[i] == "-":
            if ans =="":
                ans += s[i]
                sign = s[i]
            break
        elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
            ans += s[i]
            break
        else:
            break
    if ans == "+" or ans == "-":
        for i in range(index+1,length):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                ans += s[i]
            else:
                break
    elif ans != "":
        for i in range(index+1,length):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                ans += s[i]
            else:
                break
    if ans =="" or ans == "+" or ans == "-":
        return 0
    ret = int(ans)
    if ret < INT_MIN:
        return INT_MIN
    if ret > INT_MAX:
        return INT_MAX
    return ret

s = ["   -042","42","1337c0d3","0-1","words and 987","+0 123","+1","-+12","0   123"]
for i in s:
    print("Q :",i)
    print("Ans :",myAtoi(i))