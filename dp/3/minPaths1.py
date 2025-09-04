def minPathSum(grid: list[list[int]]) -> int:
        dp = []
        for i in range(len(grid)):
            dp.append([])
            for j in range(len(grid[0])):
                  dp[i].append(0)
        rows = len(grid) 
        cols = len(grid[0])
        INT_MAX = 400*200
        for m in range(rows):
              for n in range(cols):
                if m == 0 and n == 0 :
                    dp[m][n] = grid[m][n]
                    continue
                top = INT_MAX
                if m > 0:
                    top = dp[m-1][n]
                left = INT_MAX
                if n > 0:
                    left = dp[m][n-1]
                dp[m][n] = grid[m][n] + min(left,top)
                # print(dp,top,left,m,n)
        return dp[-1][-1]
                  
grid1 = [[1,3,1],[1,5,1],[4,2,1]]
grid2 = [[1,2,3],[4,5,6]]
print("Grid1",minPathSum(grid1))
print("Grid2",minPathSum(grid2))