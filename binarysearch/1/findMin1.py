def findMin(nums):
    left = 0
    right = len(nums)-1
    mid = int((left+right)/2)
    min_value = nums[left]
    while left <= right:
        if nums[left] <= nums[mid]:
            min_value = min(min_value,nums[left])
            left = mid + 1
        elif nums[mid] <= nums[right]:
            min_value = min(nums[mid],min_value)
            right = mid - 1
        mid = int((left+right)/2)
    return min_value

nums = [4,5,1,2,3]
print(findMin(nums))