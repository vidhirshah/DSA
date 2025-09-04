def uniquePaths( m: int, n: int) -> int:
    dp = [0]*n
    for i in range(m):
        temp = [0]*n
        for j in range(n):
            if i == 0 and j == 0:
                last = 1
                dp[j] = 1
                continue
            ans = 0
            if i > 0:
                ans += dp[j]
            if j > 0:
                ans += last
            dp[j] = ans
            last = ans
        # print(dp)
    return dp[n-1]
print(uniquePaths(3,7))