def isSubsetSum(nums):
    target = sum(nums)
    if target % 2 == 1:
        return False
    target = int(target / 2)
    dp = []
    print(target)
    for i in range(len(nums)):
        dp.append([])
        for j in range(target+1):
            dp[i].append(-1)
    def helper(index,sum):
        if sum == 0 or nums[index] == sum:
            dp[index][sum] = True
            return True
        if index == len(nums) - 1:
            return False
        if dp[index][sum] != -1:
            return dp[index][sum]
        left = False
        if nums[index] <= sum:
            left = helper(index+1,sum-nums[index]) 
        right = helper(index+1,sum)
        dp[index][sum] = left or right
        return dp[index][sum]
    return helper(0,target)

nums = [1,5,11,5]
nums = [1,2,5]
print(isSubsetSum(nums))