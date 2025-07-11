def leaders(nums):
    result = [nums[-1]]
    low = len(nums)-1
    max_no = nums[-1]
    while low > 0:
        if nums[low] > max_no:
            result.insert(0,nums[low])
            max_no = nums[low]
        low = low - 1
    return result

nums = [1, 2, 5, 3, 1, 2]
print(leaders(nums))