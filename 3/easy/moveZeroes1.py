def moveZeroes(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i] , nums[left] = nums[left] , nums[i]
            left = left + 1
    return

nums = [7,0,1,0,3,12]
moveZeroes(nums)
print(nums)