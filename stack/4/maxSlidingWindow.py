def maxSlidingWindow(nums :list[int],k):
    n = len(nums)
    if n == 1:
        return nums
    ans = []
    for i in range(n-k+1):
        maxi = nums[i]
        for j in range(k):
            if maxi < nums[i+j]:
                maxi = nums[i+j]
        ans.append(maxi)
    return ans

nums = [1, 0, -1, -3, -4, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums,k))