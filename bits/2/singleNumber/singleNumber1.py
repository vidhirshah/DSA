def singleNumber(nums):
    ans = 0
    p2 = 1
    for i in range(31):
        count = 0
        for j in nums:
            if j & (1 << i):
                count += 1
        count %= 3
        ans = ans + count*p2
        p2 <<= 1
    return ans
nums = [0,1,0,1,0,1,99]
print(singleNumber(nums))