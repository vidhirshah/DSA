def reverseWords(s):
    result = ""
    temp = ""
    for i in s:
        if i == " ":
            if result != "" :
                if temp != "":
                    result = temp + " " + result
            else:
                result = temp
            temp = ""
        else:
            temp += i
    if temp != "":
        if result != "":
            result = temp + " " + result
        else:
            result = temp
    return result 

s = "EPY2giL"
print(reverseWords(s))