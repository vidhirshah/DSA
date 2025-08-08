def canJump(nums):
    maximum = 0
    for i in range(len(nums)-1):
        if i > maximum:
            return False
        maximum = max(maximum,i + nums[i])

    if maximum >= len(nums) - 1:
        return True
    return False

nums = [3,2,1,0,4]
print(canJump(nums))