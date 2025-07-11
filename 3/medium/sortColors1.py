def sortColors(nums):
    low = -1
    high = len(nums)
    mid = 0
    while mid < high:
        if nums[mid] == 2:
            while high > 0 and nums[high-1] == 2:
                high = high - 1
            if mid != high:
                high = high - 1
                nums[high] , nums[mid] = nums[mid] , nums[high]
        if nums[mid] == 0:
            low = low + 1
            nums[low] , nums[mid] = nums[mid] , nums[low]
        if nums[mid] == 1:
            mid = mid + 1
            continue
        mid = mid + 1
    return

nums = [1,2,0]
sortColors(nums)
print(nums)