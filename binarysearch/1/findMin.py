def findMin(nums):
    left = 0
    right = len(nums)-1
    mid = int((left+right)/2)
    while left <= right:
        if left + 1 == mid and right - 1 == mid:
            return min(nums[left],nums[mid],nums[right])
        elif left == mid and mid + 1 == right:
            return min(nums[mid],nums[right])
        elif mid == left and mid == right:
            return nums[mid]
        if nums[left] <= nums[mid]:
            if nums[left] <= nums[right]:
                right = mid 
            else:
                left = mid 
        elif nums[mid] <= nums[right]:
            right = mid 
        mid = int((left+right)/2)
    return nums[mid]

nums = [4,5,1,2,3]
print(findMin(nums))