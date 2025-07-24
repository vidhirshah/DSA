def maxLen(nums):
    sum = 0 
    length = 0
    # a + k = sum
    hash = []
    start = -1
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum in hash:
            length = max(length,i-hash.index(sum))
        hash.append(sum)
    return length

nums =   [12,10,43]
print(maxLen(nums))
