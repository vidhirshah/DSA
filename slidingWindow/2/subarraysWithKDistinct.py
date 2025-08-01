def subarraysWithKDistinct(nums,k):
    count = 0
    for i in range(len(nums)):
        hash = set()
        for j in range(i,len(nums)):
            hash.add(nums[j])
            if len(hash) == k:
                count += 1
            elif len(hash) > k:
                break
    return count

nums = [1,2,1,1,3]
k = 2
print(subarraysWithKDistinct(nums,k))