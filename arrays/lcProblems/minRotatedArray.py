def findMin(nums):
    left = 0
    right = len(nums) -1
    ans = float("inf")
    while left <= right:
        mid = int((left+right)/2)
        ans = min(ans,nums[mid])
        if nums[left] == nums[mid] and nums[mid] == nums[right]:
            right -= 1
            left += 1 
        elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return ans

nums = [6,7,8,9,5,5,5]
print(findMin(nums))