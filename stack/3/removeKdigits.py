def removeKdigits(num: str , k):
    if k == len(num):
        return "0"
    temp = k
    stack = []
    for i in num:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] > i:
            while stack and stack[-1] >= i and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)
        else:
            stack.append(i)
    ans = "".join(stack)[:len(stack)-k]
    return ans.lstrip('0') or '0'

s = "1000000"
k = 3
print(removeKdigits(s,k))