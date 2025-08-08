
def frogJump(heights):
    n = len(heights)
    dp = [-1]*(n)
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2,n):
        left = dp[i-1] + abs(heights[i]-heights[i-1])
        right = dp[i-2] + abs(heights[i]-heights[i-2])
        dp[i] = min(left,right)
    return dp[n-1]

heights = [7, 5, 1, 2, 6]
print(frogJump(heights))