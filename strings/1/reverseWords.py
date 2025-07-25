def reverseWords(s):
    result = []
    temp = ""
    for i in s:
        if i == " ":
            if temp != "":
                result.append(temp)
            temp = ""
        else:
            temp += i
    result.append(temp)
    result.reverse()
    return " ".join(result)

s = "a good   example"
print(reverseWords(s))