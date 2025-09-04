def uniquePaths( m: int, n: int) -> int:
    dp = []
    for i in range(m):
        dp.append([])
        for j in range(n):
            dp[i].append(0)
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            ans = 0
            if i > 0:
                ans += dp[i-1][j]
            if j > 0:
                ans += dp[i][j-1]
            dp[i][j] = ans
    return dp[m-1][n-1]
print(uniquePaths(3,7))