def findMin(nums):
    left = 0
    right = len(nums)-1
    mid = int((left+right)/2)
    min_value = 0
    while left <= right:
        if nums[left] <= nums[mid]:
            if nums[min_value] > nums[left]:
                min_value = left
            left = mid + 1
        elif nums[mid] <= nums[right]:
            if nums[min_value] > nums[mid]:
                min_value = mid
            right = mid - 1
        mid = int((left+right)/2)
    return (len(nums) - min_value)%len(nums)

nums = [1,2,3,4,5]
print(findMin(nums))