def getCount(nums,k):
    count = 0
    left = 0
    hash = {}
    for right in range(len(nums)):
        hash[nums[right]] = 1 + hash.get(nums[right],0)
        while len(hash) > k:
            hash[nums[left]] -= 1
            if hash[nums[left]] == 0:
                hash.pop(nums[left])
            left += 1
        if len(hash) <= k:
            count += right - left + 1
        print(hash)
    return count

def subarraysWithKDistinct(nums,k):
    if k == 0:
        return getCount(nums,0)
    # print(getCount(nums,k) )
    # print(getCount(nums,k-1) )
    return getCount(nums,k) - getCount(nums,k-1)

nums = [1,2,1,2,3]
k = 2
print(nums)
print(subarraysWithKDistinct(nums,k))