import copy
def rotate(matrix):
    length = len(matrix)
    for r in range(length):
        for c in range(r+1):
            matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
    for i in range(length):
        matrix[i] = reversed(matrix[i])
    return 

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
for i in matrix:
    for j in i:
        print(j,end = " ")
    print("\n")