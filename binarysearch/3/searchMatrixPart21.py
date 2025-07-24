def searchMatrix(matrix,target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        print(row,col)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row = row + 1
        else:
            col = col - 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(searchMatrix(matrix,5))