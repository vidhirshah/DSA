def uniquePaths( m: int, n: int) -> int:
    dp = []
    for i in range(m):
        dp.append([])
        for j in range(n):
            dp[i].append(-1)
    def helper(m,n):
        if m < 0 or n < 0:
            return 0
        if m == 0 and n == 0:
            dp[0][0] = 1
            return 1
        if dp[m][n] != -1:
            return dp[m][n]
        ans = helper(m,n-1) + helper(m-1,n)
        dp[m][n] = ans
        return ans
    # if m == 1 and n == 1:
    #     return 1
    # if m < 1 or n < 1:
    #     return 0
    # ans = uniquePaths(m,n-1) + uniquePaths(m-1,n)
    return helper(m-1,n-1)

print(uniquePaths(3,7))