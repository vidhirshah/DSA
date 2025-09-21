def lengthOfLIS(nums:list):
    dp = [1]*len(nums)
    ans = 1
    n = len(nums)
    for i in range(n):
        for j in range(0,i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1,dp[i])
        ans = max(ans,dp[i])
    return ans

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))