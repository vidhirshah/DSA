def searchMatrix(matrix,target):
    for i in range(len(matrix)):
        if matrix[i][0] <= target and target <= matrix[i][-1]:
            left = 0
            right = len(matrix[i])-1
            while left <= right:
                mid = int((left+right)/2)
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(searchMatrix(matrix,20))