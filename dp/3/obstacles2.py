def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    dp = []
    for i in range(len(obstacleGrid)):
        dp.append([])
        for j in range(len(obstacleGrid[0])):
            dp[i].append(-1)
    dp[0][0] = 1
    rows = len(obstacleGrid) 
    cols = len(obstacleGrid[0]) 
    for m in range(rows):
        for n in range(cols):
            if m == 0  and n == 0:
                if obstacleGrid[m][n] != 1:
                    dp[m][n] = 1
                else:
                    dp[m][n] = 0
                continue
            if obstacleGrid[m][n] == 1:
                dp[m][n] = 0
                continue
            ans = 0
            if m > 0 :
                ans += dp[m-1][n]
            if n > 0:
                ans += dp[m][n-1]
            dp[m][n] = ans
            # print(dp)
    return dp[-1][-1]

obs1 = [[0,0,0],[0,1,0],[0,0,0]]
obs2 = [[0,1],[0,0]]
print("obs1",uniquePathsWithObstacles(obs1))
print("obs2",uniquePathsWithObstacles(obs2))