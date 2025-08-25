def largestRectArea(heights:list):
    n = len(heights)
    ans = 0
    stack = [-1]
    for i in range(n+1):
        print(i)
        while stack[-1] != -1 and (i == n or heights[stack[-1]] > heights[i]):
            left = i - stack[-2] -1 
            width = heights[stack[-1]]*(left)
            ans = max(ans,width)
            print(i,stack,ans,width,left)
            stack.pop()
        stack.append(i)
    return ans

h = [4,2,0,3,2,5]
print(largestRectArea(h))