def findTargetSumWays(nums:list,target):
    def helper(index,sum):
        if index >= len(nums):
            if sum == target:
                return 1
            else:
                return 0
        minus = helper(index+1,sum -1)
        add = helper(index+1,sum+1)
        return minus + add
    return helper(0,0)

nums = [1]
target = 1
print(findTargetSumWays(nums,target))