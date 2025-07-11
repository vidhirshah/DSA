def longestSubarray(nums,k):
    count = 0
    hash = [None]*len(nums)
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        hash[i] = sum
        if sum == k:
            count = max(count,i + 1)
        if sum in hash:
            continue
        if sum - k in hash:
            count = max(count, i - hash.index(sum - k))
    return count

print(longestSubarray([1,2,3],3))