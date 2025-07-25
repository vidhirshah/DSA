def largestOddNumber(num):
    result = ""
    for i in range(len(num)-1,-1,-1):
        if (ord(num[i]) - ord('0')) % 2 == 1:
            return num[:i] + num[i]
    return ""

num = "4206"
print(largestOddNumber(num))