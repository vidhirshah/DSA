def minPathSum(grid :list[list]):
    def helper(m,n):
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        if m >= rows and n >= cols:
               return grid[m][n]
        if m != rows and n != cols:
                ans = min(helper(m,n+1) ,helper(m+1,n))
        elif m == rows and n != cols:
                ans = helper(m,n+1)
        elif n == cols and m != rows:
                ans = helper(m+1,n)        
        return ans + grid[m][n]
    return helper(0,0)

grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))