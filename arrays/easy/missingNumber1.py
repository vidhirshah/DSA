def missingNumber(nums):
    n = len(nums)
    sum = int((n * ( n + 1) )/2)
    temp_sum = 0
    for i in nums:
        temp_sum = temp_sum + i
    return sum -temp_sum

print(missingNumber([3,0,1]))