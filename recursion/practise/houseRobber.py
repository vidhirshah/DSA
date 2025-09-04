def rob(nums:list):
    def helper(i):
        if i >= len(nums):
            return 0
        withi = nums[i] + helper(i+2)
        withouti = helper(i+1)
        return max(withi,withouti)
    return helper(0)

nums = [2,7,9,3,1]
print(rob(nums))