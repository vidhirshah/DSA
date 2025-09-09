def isSubsetSum(nums):    
    target = sum(nums)
    if target % 2 == 1:
        return False
    dp = []
    length = len(nums)
    target = int(target / 2)
    for i in range(length):
        dp.append([])
        for j in range(target+1):
            dp[i].append(False)
    for i in range(length):
        dp[i][0] = True
    if nums[0] <= target:
        dp[0][nums[0]] = True
    for index in range(1,length):
        for sum1 in range(1,target+1):
            if nums[index] == sum1:
                dp[index][sum1] = True
            left = False
            if nums[index] <= sum1:
                left = dp[index-1][sum1 -nums[index]]
            right = dp[index-1][sum1]
            dp[index][sum1] = left or right
                    # for i in dp:
                    #     print(i)
    return dp[length-1][target]

nums = [1,5,11,5]
nums = [1,2,5]
print(isSubsetSum(nums))