def singleNumber(nums):
    sum = 0
    array_sum = 0
    hash = set()
    for i in nums:
        array_sum += i
        hash.add(i)
    for i in hash:
        sum += i
    sum *= 3
    array_sum = sum -array_sum
    return int(array_sum/2)

nums = [0,1,99,1,99,1,99]
print(singleNumber(nums))