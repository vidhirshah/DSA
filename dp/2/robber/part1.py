def helper(nums,n):
    if n < 0:
        return 0
    left = helper(nums,n-2) + nums[n]
    right = helper(nums,n-3) + nums[n]
    return max(left,right)

def robber(nums):
    return max(helper(nums,len(nums)-1),helper(nums,len(nums)-2))

nums = [2,7,9,3,1]
print(robber(nums))