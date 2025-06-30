def secondLargestElement(nums):
    maximum = arr[0]
    secondLargest = -1
    for i in range(len(nums)):
        if maximum < nums[i]:
            secondLargest = maximum
            maximum = nums[i]
    return secondLargest

arr = [14,9,15,12,6,8,]
print(secondLargestElement(arr))