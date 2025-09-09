def isSubsetSum(nums):
    target = sum(nums)
    if target % 2 == 1:
        return False
    target = int(target / 2)    
    def helper(index,sum):
        if sum == 0:
            return True
        if index >= len(nums):
            return False
        return helper(index+1,sum-nums[index]) or helper(index+1,sum)
    return helper(0,target)

nums = [1,5,11,5]
nums = [1,2,3,5]
print(isSubsetSum(nums))