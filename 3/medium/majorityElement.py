def majorityElement(nums):
    count = {}
    for i in nums:
        if i in count.keys():
            count[i] = count[i] + 1
            if count[i] > int(len(nums)/2):
                return i
        else:
            count[i] = 1
    for i in count.keys():
        if count[i] > int(len(nums)/2):
            return i
    return 0

print(majorityElement([1]))