def leaders(nums):
    result = []
    for i in range(len(nums)-1):
        flag = 0
        for j in range(i+1,len(nums)):
            if nums[i] <= nums[j]:
                flag = 1
                break
        if flag == 0:
            result.append(nums[i])
    result.append(nums[-1])
    return result

nums = [-3, 4, 5, 1, -4, -5]
print(leaders(nums))