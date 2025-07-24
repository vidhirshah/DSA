def possibeSubarray(nums,maxsum):
    subarray = 1
    allocated_els = 0
    for i in nums:
        if allocated_els + i <= maxsum:
            allocated_els += i
        else:
            subarray +=1
            allocated_els = i
    return subarray

def splitArray(nums,k):
    if len(nums) < k:
        return -1
    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = int((left+right)/2)
        if possibeSubarray(nums,mid) > k:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums,k))