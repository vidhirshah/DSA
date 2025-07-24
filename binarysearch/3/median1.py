def smallerEquals(matrix,target):
    cols = len(matrix[0])
    count = 0
    for i in range(len(matrix)):
        low = 0
        high = cols - 1
        while low <= high:
            mid = int((low+high)/2)
            if matrix[i][mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        count += low
    return count

def findMedian(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    median = int((rows*cols)/2)
    low = matrix[0][0]
    high = matrix[0][cols-1]
    for i in range(rows):
        if low > matrix[i][0]:
            low = matrix[i][0]
        if high < matrix[i][cols-1]:
            high = matrix[i][cols-1]
    while low <= high:
        mid = int((low+high)/2)
        if smallerEquals(matrix,mid) <= median:
            low = mid + 1
        else:
            high = mid - 1
    return low

# matrix = [ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 
matrix = [ [1, 3, 8], [2, 3, 4], [1, 2, 5] ]
print(findMedian(matrix))