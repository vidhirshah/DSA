def parseBoolExpr(expression:str):
    stack = []
    n = len(expression)
    i = 0
    while i < n:
        if expression[i] != ")":
            stack.append(expression[i])
            i += 1
        elif expression[i] == ")":
            exp = []
            while stack and stack[-1] != "(":
                if stack[-1] == "t":
                    exp.append(True)
                elif stack[-1] == "f":
                    exp.append(False)
                elif stack[-1] == False or stack[-1] == True:
                    exp.append(stack[-1])
                stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()
            if stack:
                op = stack.pop()
            if op == "!" and len(exp) == 1:
                stack.append(not exp[0])
            elif op == "&":
                ans = exp[0]
                for j in exp:
                    ans = ans and j
                stack.append(ans)
            else:
                ans = exp[0]
                for j in exp:
                    ans = ans or j
                stack.append(ans)
            i += 1
    if stack[0] == "f":
        return False
    if stack[0] == "t":
        return True
    return stack[0]

exp = "!(&(f,t))"
print(parseBoolExpr(exp))