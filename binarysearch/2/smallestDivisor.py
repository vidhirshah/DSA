import math
def possibleThreshold(nums,divisor):
    sum = 0
    for i in nums:
        sum = sum + math.ceil(i/divisor)
    return sum

def smallestDivisor(nums,threshold):
    if threshold < len(nums):
        return -1
    left = 1
    right = max(nums)
    while left <= right:
        mid = int((left+right)/2)
        sum = possibleThreshold(nums,mid)
        if sum <= threshold:
            right = mid - 1
        else:
            left = mid + 1
    return left

nums = [1,2,5,9]
threshold = 6
print(smallestDivisor(nums,threshold))