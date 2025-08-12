def helper(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    el1 = 0
    el2 = nums[0]
    pointer = nums[1]
    for i in range(2,n):
        ans = 0
        if i-2 >= 0:
            ans = max(ans,nums[i] + el2)
        if i-3 >= 0:
            ans = max(ans,nums[i]+el1)
        ans = max(pointer,ans)
        el1 = el2
        el2 = pointer
        pointer = ans
    return ans

def rob(nums):     
    if len(nums) == 1:
        return nums[0]  
    return max(helper(nums[:len(nums)-1]),helper(nums[1:]))

nums = [1]
print(rob(nums))