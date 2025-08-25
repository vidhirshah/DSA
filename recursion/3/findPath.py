def findPath(grid):
    result = []
    def helper(row,col,path):
        if row == len(grid)-1 and col == len(grid[0])-1:
            result.append(path)
            return
        if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
            return
        if grid[row][col] == 0:
            return
        if grid[row][col] == '!':
            return
        temp = grid[row][col]
        grid[row][col] = '!'
        path = path + 'U'
        helper(row-1,col,path)
        path = path [:-1]
        path = path + 'D'
        helper(row+1,col,path)
        path = path [:-1]
        path = path + 'L'
        helper(row,col-1,path)
        path = path [:-1]
        path = path + 'R'
        helper(row,col+1,path)
        path = path [:-1]
        grid[row][col] = temp
    helper(0,0,"")
    return result

grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
print(findPath(grid))