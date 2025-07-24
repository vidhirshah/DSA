def singleNonDuplicate(nums):
    ans = 0
    left = 0
    right = len(nums) - 1
    mid = int((left+right)/2)
    if len(nums) == 1:
        return nums[0]
    while left <= right:
        mid = int((left+right)/2)
        if mid > 0 and mid < len(nums) - 1:
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] == nums[mid - 1] and mid%2 == 1:
                left = mid + 1
            elif nums[mid] == nums[mid - 1] and mid%2 == 0:
                right = mid - 1
            elif nums[mid] == nums[mid+1] and mid%2 == 1:
                right = mid - 1
            elif nums[mid] == nums[mid+1] and mid%2 == 0:
                left = mid + 1
        elif mid == 0:
            if nums[mid] != nums[mid+1]:
                return nums[mid]
            if nums[mid] == nums[mid+1] and mid%2 == 1:
                right = mid - 1
            elif nums[mid] == nums[mid+1] and mid%2 == 0:
                left = mid + 1
        if mid == len(nums) - 1:
            if nums[mid-1]!= nums[mid]:
                return nums[mid]
            if nums[mid] == nums[mid - 1] and mid%2 == 1:
                left = mid + 1
            elif nums[mid] == nums[mid - 1] and mid%2 == 0:
                right = mid - 1
    return -1

nums = [1,1,2]
print(singleNonDuplicate(nums))