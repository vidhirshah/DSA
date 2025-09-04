def minPathSum(grid: list[list[int]]) -> int:
        dp = []
        for i in range(len(grid)):
            dp.append([])
            for j in range(len(grid[0])):
                  dp[i].append(-1)
        def helper(m,n):
            rows = len(grid) - 1
            cols = len(grid[0]) - 1
            INT_MAX = 400*200
            if m > rows and n > cols:
                return INT_MAX
            if m == rows and n == cols :
                  dp[m][n] = grid[m][n]
                  return grid[m][n]
            down = INT_MAX
            if dp[m][n] != -1:
                 return dp[m][n]
            if m < rows:
                down = helper(m+1,n)
            up = INT_MAX
            if n < cols:
                up = helper(m,n+1)
            dp[m][n] = grid[m][n] + min(up,down)
            return dp[m][n]
        return helper(0,0)

grid1 = [[1,3,1],[1,5,1],[4,2,1]]
grid2 = [[1,2,3],[4,5,6]]
print("Grid1",minPathSum(grid1))
print("Grid2",minPathSum(grid2))