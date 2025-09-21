def lengthOfLIS(nums:list):
    dp = [1]*len(nums)
    prev = [-1]*len(nums)
    nums.sort()
    last_index = 0
    ans = 1
    n = len(nums)
    for i in range(n):
        index = -1
        for j in range(0,i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] =dp[j] + 1
                    index = j
        prev[i] = index
        if ans < dp[i]:
            ans = dp[i]
            last_index = i
    result = []
    while last_index != -1:
        result.insert(0,nums[last_index])
        last_index = prev[last_index]
    return result

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))