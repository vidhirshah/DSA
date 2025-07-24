def largestElement(nums):
    maximum = 0
    for i in range(len(nums)):
        if maximum < nums[i]:
            maximum = nums[i]
    return maximum

arr = [14,9,15,12,6,8,]
print(largestElement(arr))