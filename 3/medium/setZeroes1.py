def setZeroes(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    col1 = -1
    for r in range(rows):
        for c in range(col):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                if c == 0:
                    col1 = 0
                else:
                    matrix[0][c] = 0
    for r in range(1,rows):
        for c in range(1,col):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for c in range(col):
            matrix[0][c] = 0
    if col1 == 0:
        for r in range(rows):
            matrix[r][0] = 0
    return

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
for i in matrix:
    for j in i:
        print(j,end=" ")
    print("\n")