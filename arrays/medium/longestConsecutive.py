def longestConsecutive(nums):
    max_length = 1
    for i in range(len(nums)-1):
        x = nums[i]
        length = 1
        while x + 1 in nums:
            x = x + 1
            length = length + 1 
        max_length = max(length,max_length)
    return max_length

print(longestConsecutive( [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))