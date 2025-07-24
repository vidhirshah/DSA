def maxSubArray(nums):
    sum = 0
    max_sum = -10**4-1
    for i in nums:
        sum = sum + i
        max_sum = max(sum,max_sum)
        if sum < 0:
            sum = 0
    return max_sum

print(maxSubArray([-1]))