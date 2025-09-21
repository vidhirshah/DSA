def lengthOfLIS(nums:list):
    def helper(index,prev):
        if index >= len(nums):
            return 0
        nottake = helper(index+1,prev)
        take = 0
        if prev == -10**4-1 or nums[index]>prev:
            take = 1 + helper(index+1,nums[index])
        return max(take,nottake)
    return helper(0,-10**4-1)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))