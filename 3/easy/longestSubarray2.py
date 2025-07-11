def longestSubarray(nums,k):
    count = 0
    sum = 0
    i = 0
    j = 0
    while i < len(nums) and j < len(nums) and i <= j:
        while sum > k and i <=j:
            sum = sum -nums[i]
            i = i + 1
        while sum < k and j < len(nums):
            sum = sum + nums[j]
            j = j + 1
        if sum == k:
            count = max(count,j-i)
            sum = sum - nums[i]
            i = i + 1
    return count

print(longestSubarray([1,2,3],6))