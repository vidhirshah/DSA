def missingNumber(nums):
    xor1 = 0
    xor2 = 0
    for i in range(len(nums)):
        xor1 = i ^ xor1
        xor2 = nums[i] ^ xor2
    xor1 = xor1 ^ len(nums)
    return xor1 ^ xor2

print(missingNumber([2,0,1]))