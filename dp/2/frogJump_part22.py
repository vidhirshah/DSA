def frogJump(heights,k):
    INT_MAX = 2**31 -1
    n = len(heights)
    dp = [-1]*(n)
    dp[0] = 0
    for i in range(1,k):
        dp[i] = abs(heights[i] - heights[0])
    for i in range(2,n):
        ans = INT_MAX
        for j in range(1,k+1):
            if i-j >= 0:
                ans = min(ans,dp[i-j]+abs(heights[i]-heights[i-j]))
        dp[i] = ans
    return dp[n-1]

heights = [15, 4, 1, 14, 15]
k = 3
print(frogJump(heights,k))