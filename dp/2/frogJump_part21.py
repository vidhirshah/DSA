INT_MAX = 2**31-1
def helper(heights,k,n,dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    ans = INT_MAX
    for i in range(1,k+1):
        if n-i >= 0:
            ans = min(ans,helper(heights,k,n-i,dp)+abs(heights[n]-heights[n-i]))
    dp[n] = ans
    return dp[n]

def frogJump(heights,k):
    dp = [-1]*len(heights)
    return helper(heights,k,len(heights)-1,dp)

heights = [15, 4, 1, 14, 15]
k = 3
print(frogJump(heights,k))