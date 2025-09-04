def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    dp = []
    for i in range(len(obstacleGrid)):
        dp.append([])
        for j in range(len(obstacleGrid[0])):
            dp[i].append(-1)
    def helper(m,n):
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1
        if m > rows and n > cols:
            return 0
        if m == rows and n == cols:
            if obstacleGrid[m][n] != 1:
                dp[m][n] = 1
                return 1
            return 0
        if obstacleGrid[m][n] == 1:
            dp[m][n] = 0
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        ans = 0
        if m < rows :
            ans += helper(m+1,n)
        if n < cols:
            ans += helper(m,n+1)
        dp[m][n] = ans
        return ans 
    if obstacleGrid[0][0] == 1:
        return 0
    return helper(0,0)

obs1 = [[0,0,0],[0,1,0],[0,0,0]]
obs2 = [[0,1],[0,0]]
print("obs1",uniquePathsWithObstacles(obs1))
print("obs2",uniquePathsWithObstacles(obs2))