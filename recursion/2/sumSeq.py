def subsets(nums,k):
    sum = 0
    def helper(sum,i):
        if i == len(nums):
            if sum == k:
                return 1
            else:
                return 0
        sum += nums[i]
        ans = helper(sum,i+1)
        sum -= nums[i]
        ans += helper(sum,i+1)
        return ans
    return helper(0,0)

nums =  [4, 2, 10, 5, 1, 3]
k = 5
print(subsets(nums,k))