def subarraysWithXorK(nums,k):
    xor = 0 #b
    count = 0
    # k is b
    # a^k = b
    # a = b*k
    hash = {0:1}
    for i in range(len(nums)):
        xor = xor^nums[i]
        if xor^k in hash.keys():
            count = count + hash[xor^k]
        if xor in hash.keys():
            hash[xor] = hash[xor] + 1
        else:
            hash[xor] = 1
    return count

nums =  [4, 2, 2, 6, 4]
print(subarraysWithXorK(nums,4))