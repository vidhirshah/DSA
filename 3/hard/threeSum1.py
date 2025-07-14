def threeSum(nums):
    hash = set()
    result = []
    sum = 0
    for i in range(len(nums)-2):
        hash = set()
        for j in range(i + 1,len(nums)):
            if -(nums[i]+nums[j]) in hash:
                if sorted([nums[i],nums[j],-(nums[i]+nums[j])]) not in result:
                    result.append(sorted([nums[i],nums[j],-(nums[i]+nums[j])]))
            hash.add(nums[j])
    return result

nums = [0,0,0]


print(threeSum(nums))