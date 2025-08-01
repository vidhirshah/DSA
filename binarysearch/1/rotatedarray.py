def search(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = int((left+right)/2)
        if nums[mid] == target:
            return True
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        elif nums[mid] <= nums[right]:
            if nums[mid] < target and target <= nums[right]:
                left = mid +1
            else:
                right = mid - 1
    return False

nums = [1,0,1,1,1]
print(search(nums,0))