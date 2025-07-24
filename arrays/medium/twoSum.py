def twoSum(nums,k):
    for i in range(len(nums)):
        if  k - nums[i] in nums[i+1:]:
            return [i,i + 1 + nums[i+1:].index(k-nums[i])]
    return []

print(twoSum([3,3],6))