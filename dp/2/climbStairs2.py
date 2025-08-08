def climbStairs(n):
    dp = [-1]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 30
print(climbStairs(n))