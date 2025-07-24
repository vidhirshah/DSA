def majorityElement(nums):
    hash = {}
    result = []
    for i in nums:
        if i in hash.keys():
            hash[i] = hash[i] + 1
        else:
            hash[i] = 1
        if hash[i] > int(len(nums)/3) and i not in result:
            result.append(i)
    return result

nums = [3,2]
print(majorityElement(nums))