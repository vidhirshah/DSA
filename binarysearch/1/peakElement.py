def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    if len(nums) > 1:
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
    right = len(nums) - 2
    left = 1
    while left <= right:
        mid = int((left+right)/2)
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
            left = mid + 1
        elif nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

nums = [1,2,1,2,1]
print(findPeakElement(nums))