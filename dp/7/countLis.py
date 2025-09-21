def lengthOfLIS(nums:list):
    dp = [1]*len(nums)
    count = [1]*len(nums)
    count[0] = 1
    ans = 1
    index = 0
    n = len(nums)
    for i in range(n):
        for j in range(0,i):
            if nums[j] < nums[i]:
                local_ans = dp[j] + 1
                if dp[i] == local_ans:
                    count[i] += count[j]
                elif dp[i] < local_ans:
                    count[i] = count[j]
                dp[i] = max(dp[j] + 1,dp[i])
        ans = max(ans,dp[i])
    total_count = 0
    for i in range(len(dp)):
        if dp[i] == ans:
            total_count += count[i]
    return total_count

nums = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))