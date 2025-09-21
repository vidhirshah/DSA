def largestRectArea(heights:list):
    n = len(heights)
    def pse():
        stack = []
        result = [0]*len(heights)
        for i in range(len(heights)):
            if len(stack) == 0:
                result[i] = -1
            elif heights[i] > heights[stack[-1]]:
                result[i] = stack[-1]
            else:
                while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = -1
                else:
                    result[i] = stack[-1]
            stack.append(i)
        return result
    def nse():
        stack = []
        result = [0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            if len(stack) == 0:
                result[i] = len(heights)
            elif heights[i] > stack[-1][0]:
                result[i] = stack[-1][1]
            else:
                while len(stack) != 0 and heights[i] <= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = len(heights)
                else:
                    result[i] = stack[-1][1]
            stack.append([heights[i],i])
        return result
    h_pse = pse()
    h_nse = nse()
    # print(heights)
    # print(h_pse)
    # print(h_nse)
    ans = 0
    for i in range(n):
        width = heights[i]*((i -h_pse[i]) + h_nse[i] -i -1) 
        # print(heights[i],i -h_pse[i] , h_nse[i] -i-1)
        ans = max(ans,width)
    print(h_nse)
    print(h_pse)
    return ans

h = [2,1,5,6,2,3]
print(largestRectArea(h))