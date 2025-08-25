def combinationSum(nums,target):
    result = []
    subseaq = []
    nums.sort()
    def helper(sum,i):
        if i == len(nums):
            result.append(subseaq[:])
            return 
        subseaq.append(nums[i])
        helper(sum+nums[i],i+1)
        while i < len(nums)-1 and nums[i] == nums[i+1]:
             i += 1       
        subseaq.pop()
        helper(sum,i+1)
    helper(0,0)
    return result

nums = [1,2,2]
target = 8
print(combinationSum(nums,target))