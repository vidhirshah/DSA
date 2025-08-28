def isHeap(nums):
    n = len(nums)
    i = 0
    while i < int(n/2) + 1:
        left = 2*i + 1
        right = 2*i + 2
        if left < n and nums[left] < nums[i]:
            return False
        if right < n and nums[right] < nums[i]:
            return False
        i += 1
    return True

nums =   [10, 20, 30, 25, 15]
print(isHeap(nums))