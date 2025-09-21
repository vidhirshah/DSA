def matrixMultiplication(nums):
    dp = []
    for i in range(len(nums)):
        dp.append([])
        for j in range(len(nums)):
            dp[i].append(-1)
    def helper(left,right):
        if left == right:
            return 0
        if dp[left][right] != -1:
            return dp[left][right]
        mini = 1e9
        for i in range(left,right):
            part1 = helper(left,i)
            part2 = helper(i+1,right)
            part3 = nums[left-1]*nums[i]*nums[right]
            mini = min(part1+part2+part3,mini)
        dp[left][right] = mini
        return mini
    return helper(1,len(nums)-1)

nums =  [10, 15, 20, 25]
print(matrixMultiplication(nums))