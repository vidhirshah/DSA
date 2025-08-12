def helper(nums,n):
    if n < 0:
        return 0
    # print(nums,n)
    left = nums[n]+helper(nums,n-2)
    right = helper(nums,n-1)
    return max(left,right)

def robber(nums):
    return max(helper(nums[0:len(nums)-1],len(nums)-2),helper(nums[1:],len(nums)-2))

nums = [1,2,3,1]
print(robber(nums))