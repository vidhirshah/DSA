def getCount(nums,k):
    count = 0
    left = 0
    odds = 0
    for right in range(len(nums)):
        odds += nums[right] % 2
        while odds > k:
            odds -= nums[left] %2
            left += 1
        if odds <= k:
            count += right - left + 1
    return count


def numSubarraysWithSum(nums,k):
    if k == 0:
        return getCount(nums,k)
    return getCount(nums,k) - getCount(nums,k-1)

nums = [1,1,2,1,1]
k = 3
print(numSubarraysWithSum(nums,k))