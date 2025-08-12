def robber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    dp = [-1]*n
    dp[0] = nums[0]
    dp[1] = nums[1]
    left = 0
    right = 0
    for i in range(2,n):
        if i - 2 >= 0:
            left = nums[i] + dp[i-2]
        else:
            left = 0
        if i -3 >= 0:
            right = nums[i] + dp[i-3]
        else:
            right = 0
        dp[i] = max(left,right)
    return max(dp[n-1],dp[n-2])

nums = [1,2,3,1]
print(robber(nums))