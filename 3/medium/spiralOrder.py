def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    top = 0
    buttom = m -1
    left = 0
    right = n - 1
    while top<=buttom and left <= right:
        for i in range(left,right+ 1):
            result.append(matrix[top][i])
        top = top + 1
        for i in range(top,buttom+1):
            result.append(matrix[i][right])
        right = right - 1
        if top <= buttom:
            for i in range(right,left-1,-1):
                result.append(matrix[buttom][i])
            buttom = buttom - 1
        if left <= right:
            for i in range(buttom,top-1,-1):
                result.append(matrix[i][left])
            left = left + 1
    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))