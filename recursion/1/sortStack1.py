def sort_insert(stack,element):
    if len(stack) <= 0 or element < stack[-1]:
        stack.append(element)
        return
    temp = stack.pop()
    sort_insert(stack,element)
    stack.append(temp)
    return

def sortStack(stack):
    if len(stack) <= 1:
        return stack
    temp = stack.pop()
    # print(stack,temp)
    sortStack(stack)
    sort_insert(stack,temp)
    return stack

stack = [1,5,3,6,8,6,4,3,5,4,5,3,6,5,7,9,0,2]
# stack = [1,2,3,4]
sortStack(stack)
print(stack)