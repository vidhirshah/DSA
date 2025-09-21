def lengthOfLIS(nums:list):
    dp = [1]*len(nums)
    ans = 1
    n = len(nums)
    for i in range(n):
        for j in range(0,i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1,dp[i])
    dp_back = [1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(len(nums)-1,i,-1):
            if nums[j] < nums[i]:
                dp_back[i] = max(dp_back[j] + 1,dp_back[i])
        ans = max(dp[i]+dp_back[i]-1,ans)
    return ans

nums = [5, 1, 4, 2, 3, 6, 8, 7]
print(lengthOfLIS(nums))