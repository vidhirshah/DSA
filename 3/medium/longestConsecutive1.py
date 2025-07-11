def longestConsecutive(nums):
    max_length = 1
    length = 1
    nums = sorted(nums)
    x = nums[0]
    for i in nums[1:]:
        if i == x + 1:
            length = length + 1
        else:
            length = 1
            max_length = max(length,max_length)
        x = i
    return max(max_length,length)

print(longestConsecutive( [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))