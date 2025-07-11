def rearrangeArray(nums):
    positive = []
    negative = []
    for i in nums:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    for i in range(int(len(nums)/2)):
        nums[2*i] = positive[i]
        nums[2*i + 1] = negative[i]
    return


nums = [3,1,-2,-5,2,-4]
rearrangeArray(nums)
print(nums)