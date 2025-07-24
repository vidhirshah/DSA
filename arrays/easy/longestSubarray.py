def longestSubarray(nums,k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        if nums[i] > k:
            continue
        for j in range(i,len(nums)):
            sum = sum + nums[j]
            if sum == k:
                count = max(count , j - i + 1)
            if sum > k:
                break
    return count

print(longestSubarray([10, 5, 2, 7, 1, 9],15))