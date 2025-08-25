def minimalRect(matrix:list[list[str]]):
    def largestRectArea(heights:list):
        n = len(heights)
        ans = 0
        stack = [-1]
        for i in range(n+1):
            while stack[-1] != -1 and (i == n or heights[stack[-1]] > heights[i]):
                left = i - stack[-2] -1 
                width = heights[stack[-1]]*(left)
                ans = max(ans,width)
                stack.pop()
            stack.append(i)
        return ans
    m = len(matrix)
    n = len(matrix[0])
    temp_matrix = []
    temp_matrix.append([])
    for j in range(n):
        if matrix[0][j] == "0":
            temp_matrix[0].append(0)
        else:
            temp_matrix[0].append(1)
    ans = largestRectArea(temp_matrix[0])
    for i in range(1,m):
        temp_matrix.append([])
        for j in range(n):
            if matrix[i][j] == "0":
                temp_matrix[i].append(0)
            else:
                temp_matrix[i].append(temp_matrix[i-1][j] + 1)
        ans = max(largestRectArea(temp_matrix[i]),ans)
    return ans

matrix = [["1"]]
print(minimalRect(matrix))