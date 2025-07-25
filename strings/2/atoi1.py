def myAtoi(s):
    INT_MAX = 2**31 -1
    INT_MIN = -2**31
    length = len(s)
    if length == 0:
        return 0
    ans = ""
    index = 0
    while index < length and s[index] == " ":
        index += 1
    sign = 1
    if s[index] == "-":
        sign = -1
        index += 1
    elif s[index] == "+":
        index +=1
    while index < length:
        if ord(s[index]) >= 48 and ord(s[index]) <= 57:
            ans += s[index]
        else:
            break
        index += 1
    if ans =="" or ans == "+" or ans == "-":
        return 0
    ret = sign*int(ans)
    if ret < INT_MIN:
        return INT_MIN
    if ret > INT_MAX:
        return INT_MAX
    return ret

s = ["   -042","42","1337c0d3","0-1","words and 987","+0 123","+1","-+12","0   123","-91283472332"]
for i in s:
    print("Q :",i)
    print("Ans :",myAtoi(i))
# print(myAtoi("42"))