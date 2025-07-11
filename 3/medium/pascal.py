def pascal(numRows):
    if numRows <= 1:
        result = [[1]]
    else:
        result = [[1],[1,1]]
    for i in range(3,numRows+1):
        result.append([0]*i)
        result[i-1][0] = 1
        result[i-1][i-1] = 1
        for j in range(1,i-1):
            result[i-1][j] = result[i-2][j-1] + result[i-2][j]
    return result

print(pascal(2))