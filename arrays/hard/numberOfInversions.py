def numberOfInversions(nums):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                count = count + 1
    return count

nums = [2, 3, 7, 1, 3, 5]
# nums = [-10, -5, 6, 11, 15, 17]
print(numberOfInversions(nums))