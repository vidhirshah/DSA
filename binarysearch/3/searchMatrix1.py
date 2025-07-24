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

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix,3))