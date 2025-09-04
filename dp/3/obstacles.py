def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    def helper(m,n):
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1
        if m > rows and n > cols:
            return 0
        if m == rows and n == cols:
            if obstacleGrid[m][n] != 1:
                return 1
            return 0
        if obstacleGrid[m][n] == 1:
            return 00
        ans = 0
        if m < rows :
            ans += helper(m+1,n)
        if n < cols:
            ans += helper(m,n+1                                                         )
        return ans 
    if obstacleGrid[0][0] == 1:
        return 0
    return helper(0,0)

obs = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles([[0,1],[0,0]]))