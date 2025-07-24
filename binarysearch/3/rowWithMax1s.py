def rowWithMax1s(mat):
    max_index = -1
    max_count = -1
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[i])):
            count += mat[i][j]
        if count > max_count:
            max_count = count
            max_index = i
    return max_index

mat = [  [0, 0, 1],[1,1,1], [1, 1, 1] ]
print(rowWithMax1s(mat))

    # left = 0
    # right = len(mat) - 1
    # if len(mat) == 0:
    #     return -1
    # while left <= right:
    #     mid = int((left+right)/2)
    #     if mat[mid] == 1:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # if left >= len(mat)  :
    #     return -1
    # return left
