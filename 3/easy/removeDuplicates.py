def removeDuplicates(nums):
    pointer = 0
    count = 1
    for i in range(len(nums)):
        if nums[pointer] == nums[i]:
            continue
        else:
            pointer = pointer + 1
            nums[pointer] = nums[i]
            count = count + 1
    return count
n = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(n))
print(n)