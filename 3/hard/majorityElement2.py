def majorityElement(nums):
    count1 = 0
    el1 = None
    count2 = 0
    el2 = None
    for i in nums:
        if count1 == 0 and i != el2:
            count1 = count1 + 1
            el1 = i
        elif count2 == 0 and i != el1:
            count2 = count2 + 1
            el2 = i
        elif el1 == i:
            count1 = count1 + 1
        elif el2 == i:
            count2 = count2 + 1
        else:
            count1 = count1 - 1
            count2 = count2 - 1
    result = []
    count 1 =0 
    count2 = 0
    for i in nums:
        if i == el1:
            count1 = count1 + 1
        if i == el2:
            count2 = count2 + 1
    if count1 > int(len(nums)/3):
        result.append(el1)
    if count2 > int(len(nums)/3):
        result.append(el2)
    return result

nums = [3,2,3]
print(majorityElement(nums))