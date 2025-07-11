def nextPermutation(nums):
    dip = -1
    for i in range(len(nums) - 2,-1,-1):
        if nums[i] < nums[i+1]:
            dip = i
            break
    if dip == -1:
        nums = nums.reverse()
        return
    for i in range(len(nums) - 1 , dip,-1):
        if nums[i] > nums[dip]:
            nums[i] , nums[dip] = nums[dip] , nums[i]
            break
    count = 0
    for i in range(dip+1,int((dip+1+len(nums))/2)):
        nums[i] , nums[len(nums)-1-count] = nums[len(nums)-1-count] , nums[i]
        count = count + 1
    return

nums = [4, 3, 6, 7, 5, 2, 1]
nextPermutation(nums)
print(nums)


# (4, 3, 6, 2, 5, 1, 7)
# (4, 3, 6, 2, 5, 7, 1)
# (4, 3, 6, 2, 7, 1, 5)
# ()
# (4, 3, 6, 5, 1, 2, 7)
# (4, 3, 6, 5, 1, 7, 2)
# (4, 3, 6, 5, 2, 1, 7)
# (4, 3, 6, 5, 2, 7, 1)
# (4, 3, 6, 5, 7, 1, 2)
# (4, 3, 6, 5, 7, 2, 1)
# (4, 3, 6, 7, 1, 2, 5)
# (4, 3, 6, 7, 1, 5, 2)
# (4, 3, 6, 7, 2, 1, 5)
# (4, 3, 6, 7, 2, 5, 1)
# (4, 3, 6, 7, 5, 1, 2)
# ()
# (4, 3, 7, 1, 2, 5, 6)
# (4, 3, 7, 1, 2, 6, 5)
