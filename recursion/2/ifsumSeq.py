def subsets(nums,k):
    sum = 0
    def helper(sum,i):
        if i == len(nums):
            if sum == k:
                return True
            else:
                return False
        sum += nums[i]
        ans = helper(sum,i+1)
        sum -= nums[i]
        ans |= helper(sum,i+1)
        return ans
    return helper(0,0)

nums =  [4, 3, 9, 2] 
k = 10
print(subsets(nums,k))