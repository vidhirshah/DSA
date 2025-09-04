def minFallingPathSum(matrix):
    dp = []
    length = len(matrix)
    for i in range(length):
        dp.append([])
        for j in range(length):
            dp[i].append(-1)
    INT_MAX = 10**5
    for m in range(length):
        for n in range(length):
            if m == 0 :
                dp[m][n] = matrix[m][n]
                continue
            down = INT_MAX
            left = INT_MAX
            right = INT_MAX
            if m > 0:
                down = dp[m-1][n]
                if n > 0:
                    left = dp[m-1][n-1]
                if n < length - 1:
                    right = dp[m-1][n+1]
            dp[m][n] = matrix[m][n] + min(down,left,right)
            # print(m,n,dp)
    return min(dp[-1])

mat1 = [[2,1,3],[6,5,4],[7,8,9]]
mat2 = [[-19,57],[-40,-5]]
print("mat1",minFallingPathSum(mat1))
print("mat2",minFallingPathSum(mat2))