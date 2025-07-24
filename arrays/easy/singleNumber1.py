def singleNumber(nums):
    hash = [0]*(max(nums)+1)
    for i in nums:
        hash[i] = hash[i] + 1
    for i in hash:
        if i == 1:
            return i
    return xor

print(singleNumber([4,1,2,1,2]))