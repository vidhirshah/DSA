def removeOuterParentheses(s):
    count = 0
    index = 0
    result = []
    for i in range(len(s)):
        if s[i] == "(":
            if count == 0:
                index = i
            count += 1
        if s[i] == ")":
            count -= 1
            if count == 0 and index + 1 != i:
                result.append(s[index+1:i])
    return ''.join(result)

s = "(()())(())"
print(removeOuterParentheses(s))