def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    def helper(m,n):
        rows = len(obstacleGrid) - 1
        cols = len(obstacleGrid[0]) - 1
        if m >= rows and n >= cols:
                if obstacleGrid[m][n] == 0:
                    return 1
                return 0
        ans = 0
        if m != rows and n != cols:
            if obstacleGrid[m][n + 1] != 1:
                ans += helper(m,n+1) 
            if obstacleGrid[m+1][n] != 1:
                ans += helper(m+1,n)
        elif m == rows and n != cols:
            if obstacleGrid[m][n+1] != 1:
                ans = helper(m,n+1)
        elif n == cols and m != rows:
            if obstacleGrid[m+1][n] != 1:
                ans = helper(m+1,n)        
        return ans 
    return helper(0,0)


obstacleGrid = [[1,0]]
print(uniquePathsWithObstacles(obstacleGrid))