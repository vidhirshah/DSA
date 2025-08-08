def helper(heights,n,dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = helper(heights,n-1,dp) + abs(heights[n]-heights[n-1])
    if n != 1:
        right = helper(heights,n-2,dp) + abs(heights[n]-heights[n-2])
        dp[n] = min(left,right)
    else:
        return left
    return dp[n]

def frogJump(heights):
    dp = [-1]*len(heights)
    return helper(heights,len(heights)-1,dp)

heights = [2, 1, 3, 5, 4]
print(frogJump(heights))