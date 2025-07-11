def rearrangeArray(nums):
    temp_array = [0]*len(nums)
    positive = 0
    negative = 1
    for i in nums:
        if i > 0:
            temp_array[positive] = i
            positive = positive + 2
        else:
            temp_array[negative] = i
            negative = negative + 2
    return temp_array


nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
