def maxSubArray(nums):
    sum = 0
    max_sum = -10**4-1
    result =[0,0]
    start = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > max_sum:
            max_sum = sum
            result[1] = i
            result[0] = start
        if sum < 0:
            sum = 0
            if i < len(nums) - 1:
                start = i + 1
    return result

print(maxSubArray([5,4,-1,7,8]))