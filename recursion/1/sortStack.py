def sortStack(stack):
    if len(stack) <= 1:
        return stack
    temp = stack[-1]
    temp_stck = []
    for i in range(len(stack)-1):
        temp = stack.pop()
        if temp > stack[-1] :
            temp_stck.append(stack.pop())
            stack.append(temp)
        else:
            temp_stck.append(temp)
    stack.extend(sortStack(temp_stck))
    return stack

stack = [1,5,3,6,8,6,4,3,5,4,5,3,6,5,7,9,0,2]
# stack = [3,4,1,2]
sortStack(stack)
print(stack)