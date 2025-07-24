def sortColors(nums):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in nums:
        if i == 0:
            count0 = count0 + 1
        elif i == 1:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    for i in range(count0):
        nums[i] = 0
    for i in range(count0 ,count0+count1):
        nums[i] = 1
    for i in range(count0+count1,count0+count1+count2):
        nums[i] = 2
    return

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)