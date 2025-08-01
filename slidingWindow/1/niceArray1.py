def numberOfSubarrays(nums,k):
    count = 0
    hash = {0:1}
    odds = 0
    for i in range(len(nums)):
        odds += nums[i]%2
        req = odds - k
        count += hash.get(req,0)
        hash[odds] = 1 + hash.get(odds,0)
    return count

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums,k))