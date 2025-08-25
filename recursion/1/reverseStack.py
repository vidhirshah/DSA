def stack_reverse(stack,element):
    if len(stack) <= 0:
        stack.append(element)
        return
    temp = stack.pop()
    stack_reverse(stack,element)
    stack.append(temp)
    return

def reverseStack(stack):
    if len(stack) <= 0:
        return
    temp = stack.pop()
    reverseStack(stack)
    stack_reverse(stack,temp)
    return

stack = [1,2,3,4]
print(reverseStack(stack))
print(stack)