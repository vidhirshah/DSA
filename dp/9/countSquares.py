def countSquares(matrix:list[list]):
    count = 0
    dp = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        dp.append([])
        for j in range(n):
            if (i == 0 or j == 0):
                dp[i].append(matrix[i][j])
                count += matrix[i][j]
            else:
                dp[i].append(0)
        print(dp[i])
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
            count += dp[i][j]
    return count

matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(countSquares(matrix))