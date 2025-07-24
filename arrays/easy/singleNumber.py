def singleNumber(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor

print(singleNumber([4,1,2,1,2]))