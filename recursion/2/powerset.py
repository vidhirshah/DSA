def subsets(nums):
    res = []
    subset = []
    def helper(i):
        if i == len(nums):
            res.append(subset[:])
            return
        subset.append(nums[i])
        helper(i+1)
        subset.pop()
        helper(i+1)
    helper(0)
    return res

nums = [1,2,3]
print(subsets(nums))