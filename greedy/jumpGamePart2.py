def canJump(nums):
    jumps = 0
    left = 0
    right = 0
    maximum = 0
    while right < len(nums)-1:
        for i in range(left,right+1):
            maximum = max(maximum,left+nums[left])
        jumps += 1
        left = right + 1
        right = maximum
    return jumps

nums = [2,3,1,1,4]
print(canJump(nums))