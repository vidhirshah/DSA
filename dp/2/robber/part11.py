def helper(nums,n,dp):
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = helper(nums,n-2,dp) + nums[n]
    right = helper(nums,n-3,dp) + nums[n]
    dp[n] = max(left,right)
    return dp[n]

def robber(nums):
    dp = [-1]*(len(nums))
    return max(helper(nums,len(nums)-1,dp),helper(nums,len(nums)-2,dp))

nums = [1,2,3,1]
print(robber(nums))