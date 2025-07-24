def searchMatrix(matrix,target):
    for i in matrix:
        for j in i:
            if j == target:
                return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix,13))