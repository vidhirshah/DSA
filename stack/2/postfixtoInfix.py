def postfixToInfix(s):
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            stack.append("(" + t1 + i + t2 +")")
    return stack.pop()        

s = "abcd^e-fgh*+^*+i-"
s = "ab+"
print(postfixToInfix(s))