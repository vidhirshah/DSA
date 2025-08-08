def frogJump(heights):
    n = len(heights)
    el1 = 0
    el2 = abs(heights[0]-heights[1])
    temp = 0
    print(el1,el2)
    for i in range(2,n):
        left = el2 + abs(heights[i-1]-heights[i])
        right = el1 + abs(heights[i-2]-heights[i])
        temp = min(left,right)
        el1 = el2
        el2 = temp
        print(el1,el2)
    return temp

heights =  [10, 5, 20, 0, 15]
print(frogJump(heights))