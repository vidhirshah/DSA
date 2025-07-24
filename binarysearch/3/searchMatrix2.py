def searchMatrix(matrix,target):
    left = 0
    len1 = len(matrix)
    len2 = len(matrix[0])
    right = len1*len2
    while left <= right:
        mid = int((left+right)/2)
        index1 = int(mid/len2)
        index2 = mid % len2
        if matrix[index1][index2] == target:
            return True
        elif matrix[index1][index2] > target:
            right
    return False

matrix = [[1,3]]

print(searchMatrix(matrix,3))