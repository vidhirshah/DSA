def numSubarraysWithSum(nums,goal):
    count = 0
    hash = {0:1}
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        req = sum - goal
        count += hash.get(req,0)
        hash[sum] = 1 + hash.get(sum,0)
    return count

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums,goal))