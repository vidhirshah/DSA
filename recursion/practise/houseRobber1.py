def rob(nums:list):
    def helper(array):
        if not array:
            return 0
        withi = array[0] + helper(array[2:])
        withouti = helper(array[1:])
        return max(withi,withouti)
    return max(helper(nums[0:len(nums)-1]),helper(nums[1:]))

nums = [1,2,3,1]
print(rob(nums))