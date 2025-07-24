def majorityElement(nums):
    hash = {}
    result = []
    for i in nums:
        if i in hash.keys():
            hash[i] = hash[i] + 1
        else:
            hash[i] = 1
    for i in hash.keys():
        if hash[i] > int(len(nums) /3) :
            result.append(i)
    return result

nums = [3,2]
print(majorityElement(nums))