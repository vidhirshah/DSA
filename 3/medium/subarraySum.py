def subarraySum(nums,k):
    count = 0
    presum = 0
    hash = {0:1}
    for i in nums:
        presum = presum + i
        if presum - k in hash.keys():
            count = count + hash[presum-k]
        if presum in hash.keys():
            hash[presum] = hash[presum] + 1
        else:
            hash[presum] = 1
    return count

print(subarraySum([1,2,3,-3],3))