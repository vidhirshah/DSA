def getCount(nums,goal):
    count = 0
    left = 0
    sum = 0
    for right in range(len(nums)):
        sum += nums[right]
        while sum > goal:
            sum -= nums[left]
            left += 1
        if sum <= goal:
            count += right - left + 1
    return count


def numSubarraysWithSum(nums,goal):
    if goal == 0:
        return getCount(nums,goal)
    return getCount(nums,goal) - getCount(nums,goal-1)

nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums,goal))