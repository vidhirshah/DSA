def maxDepth(s):
    count = 0
    depth = 0
    for i in s:
        if i == "(":
            count += 1
            depth = max(count,depth)
        elif i == ")":
            count -= 1
    return depth

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))