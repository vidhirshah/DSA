def minFallingPathSum(matrix):
    dp = []
    length = len(matrix)
    for i in range(length):
        dp.append([])
        for j in range(length):
            dp[i].append(-1)
    def helper(m,n):
        rows = len(matrix)
        INT_MAX = 10**5
        if m >= rows or n >= rows:
            return INT_MAX
        if m == rows - 1:
            dp[m][n] = matrix[m][n]
            return matrix[m][n]
        if dp[m][n] != -1:
            return dp[m][n]
        down = INT_MAX
        down = helper(m+1,n)
        left = INT_MAX
        right = INT_MAX
        left = helper(m+1,n-1)
        right = helper(m+1,n+1)
        dp[m][n] = matrix[m][n] + min(down,left,right)
        return dp[m][n]
    mini = 10**5
    for i in range(len(matrix)):
        mini = min(mini,helper(0,i))
    return mini

mat1 = [[2,1,3],[6,5,4],[7,8,9]]
mat2 = [[-19,57],[-40,-5]]
print("mat1",minFallingPathSum(mat1))
print("mat2",minFallingPathSum(mat2))