def postfixToInfix(s):
    stack = []
    for i in s[::-1]:
        if i.isalnum():
            stack.append(i)
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append("(" + t1 + i + t2 +")")
    return stack.pop()        

s = "+-*+abcdf"
print(postfixToInfix(s))