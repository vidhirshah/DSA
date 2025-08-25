def singleNumber(nums):
    xor = 0
    for i in nums:
        xor ^= i
    xor = (xor & (xor-1))^xor
    bit0 = 0
    bit1 = 0
    for i in nums:
        if i & xor :
            bit1 ^= i
        else:
            bit0 ^= i
    return [bit0,bit1]

nums = [1,2,1,3,2,5]
print(singleNumber(nums))