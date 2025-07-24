def ifPlaced(nums,k,distance):
    count = 1
    last = 0
    for j in range(1,len(nums)):
        if nums[j] - nums[last] >= distance:
            count +=1
            last = j
        if count == k:
            return True
    return False


def aggressiveCows(nums,k):
    nums.sort()
    left = 1
    right = max(nums)-min(nums)
    while left<= right:
        mid = int((left+right)/2)
        if ifPlaced(nums,k,mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

nums = [4, 2, 1, 3, 6]
k = 2
print(aggressiveCows(nums,k))
