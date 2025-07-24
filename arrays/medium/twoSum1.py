def twoSum(nums,k):
    hash = [None]*len(nums)
    for i in range(len(nums)):
        hash[i] = k - nums[i]
        if nums[i] in hash[0:i]:
            return [hash.index(nums[i]),i]
    return []
print(twoSum([2,7,11,15],9))