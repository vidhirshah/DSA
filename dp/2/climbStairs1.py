def helper(n,dp):
    if n == 0:
        return 1
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    dp[n] = helper(n-1,dp) + helper(n-2,dp) 
    return dp[n]

def climbStairs(n):
    dp = [-1]*(n+1)
    return helper(n,dp)

n = 30
print(climbStairs(n))