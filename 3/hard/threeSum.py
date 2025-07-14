def threeSum(nums):
    result = []
    sum = 0
    for i in range(len(nums)-2):
        for j in range(i + 1,len(nums)-1):
            for k in range(j + 1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    if sorted([nums[i],nums[j],nums[k]]) not in result:
                        result.append(sorted([nums[i],nums[j],nums[k]]))
    return result

nums = [1,-1,-1,0]
print(threeSum(nums))