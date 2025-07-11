def majorityElement(nums):
    count = 0
    element = nums[0]
    for i in nums:
        if count == 0:
            element = i
        if element == i:
            count = count + 1
        else:
            count = count - 1
    count = 0
    for i in nums:
        if element == i:
            count = count +  1
    if count > int(len(nums)/2):
        return element
    return 

print(majorityElement([2,2,1,1,1,2,2]))