def setZeroes(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    for i in range(rows):
        for j in range(col):
            if matrix[i][j] == 0:
                for c in range(col):
                    if matrix[i][c] != 0:
                        matrix[i][c] = -1
                for r in range(rows):
                    if matrix[r][j] != 0:
                        matrix[r][j] = -1
    for i in range(rows):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
for i in matrix:
    for j in i:
        print(j,end=" ")
    print("\n")