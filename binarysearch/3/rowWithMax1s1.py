def rowWithMax1s(mat):
    max_index = -1
    max_count = 0
    for i in range(len(mat)):
        left = 0
        right = len(mat[i]) - 1
        while left <= right:
            mid = int((left+right)/2)
            if mat[i][mid] == 1:
                right = mid - 1
            else:
                left = mid + 1
        if max_count < len(mat[i]) - left:
            max_count = len(mat[i]) - left
            max_index = i
    return max_index

mat = [  [0, 0, 1],[1,1,1], [1, 1, 1] ]
print(rowWithMax1s(mat))

