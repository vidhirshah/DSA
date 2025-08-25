def singleNumber(nums):
    nums.sort()
    i = 1
    n = len(nums)
    print(nums)
    if n == 1:
        return nums[0]
    while i < n:
        print(i,nums[i],nums[i-1],nums[i+1])
        if nums[i-1] == nums[i] and nums[i+1] == nums[i]:
            i += 3
        elif nums[i+1] != nums[i]:
            return nums[i+1]
        else:
            return nums[i-1]
    return nums[-1]

nums = [30000,500,100,30000,100,30000,100]
print(singleNumber(nums))