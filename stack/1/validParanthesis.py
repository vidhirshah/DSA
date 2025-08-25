def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if len(stack) <=  0:
                return False
            element = stack.pop()
            if (i == ")" and element == "(") or (i == "]" and element == "[") or (i == "}" and element == "{"):
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    return False

s = "(]"
print(isValid(s))