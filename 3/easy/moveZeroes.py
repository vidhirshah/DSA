def moveZeroes(nums):
    count = 0
    pointer = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count = count + 1
        else:
            nums[pointer] = nums[i]
            pointer = pointer + 1
    for i in range(count):
        nums[pointer] = 0
        pointer = pointer + 1
    return
nums = [7,0,1,0,3,12]
moveZeroes(nums)
print(nums)