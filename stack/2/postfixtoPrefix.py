def postfixToInfix(s):
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            stack.append(i + t1  + t2 )
    return stack.pop()        

s = "ab-de+f*/"
print(postfixToInfix(s))