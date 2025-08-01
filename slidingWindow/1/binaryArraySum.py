def numSubarraysWithSum(nums,goal):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == goal:
                count += 1
            elif sum > goal:
                break
    return count

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums,goal))