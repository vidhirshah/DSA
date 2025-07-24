def reversePairs(nums):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] > 2 *nums[j]:
                count = count + 1
    return count

nums = [1,3,2,3,1]
print(reversePairs(nums))