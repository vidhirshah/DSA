def findPeakGrid(mat):
    rows = len(mat)
    cols = len(mat[0])
    low = 0
    high = len(mat[0]) - 1
    while low <= high:
        mid = int((low+high)/2)
        max_elt = -1
        max_index = mat[0][mid]
        for i in range(0,rows):
            print(mat[i][mid])
            if mat[i][mid] > max_elt:
                max_elt = mat[i][mid]
                max_index = i
        if mid == 0:
            left = -1
        else:
            left = mat[max_index][mid - 1]
        if mid == cols - 1:
            right = -1
        else:
            right = mat[max_index][mid + 1]
        if mat[max_index][mid] > left and mat[max_index][mid] > right:
            return (max_index,mid)
        elif left  > mat[max_index][mid]:
            high = mid - 1
        else: 
            low = low + 1
    return

mat = [[1,4],[3,2]]
print(findPeakGrid(mat))