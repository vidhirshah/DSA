def getPriority(x):
    if x == "^":
        return 3
    if x == "*" or x == "/":
        return 2
    if x == "+"or x =="-":
        return 1
    return -1

def infixToPostfix(s):
    ans = ""
    stack = []
    for i in s:
        if i.isalnum():
            ans += i
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while len(stack) != 0 and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
        else:
            while len(stack) != 0 and getPriority(stack[-1]) >= getPriority(i):
                ans += stack.pop()
            stack.append(i)
    while len(stack) > 0:
        ans += stack.pop()
    return ans

s = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPostfix(s))
print("abcd^e-fgh*+^*+i-")