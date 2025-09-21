def matrixMultiplication(nums):
    dp = []
    for i in range(len(nums)):
        dp.append([])
        for j in range(len(nums)):
            dp[i].append(10e9)
    for i in range(len(nums)):
        dp[i][i] = 0
    for i in range(len(nums)-1,0,-1):
        for j in range(i+1,len(nums)):
            for k in range(i,j):
                p1 = dp[i][k]
                p2 = dp[k+1][j]
                p3 = nums[i-1]*nums[k]*nums[j]
                dp[i][j] = min(p1+p2+p3,dp[i][j]) 
    return dp[1][len(nums)-1]
    # def helper(left,right):
    #     if left == right:
    #         return 0
    #     if dp[left][right] != -1:
    #         return dp[left][right]
    #     mini = 1e9
    #     for i in range(left,right):
    #         part1 = helper(left,i)
    #         part2 = helper(i+1,right)
    #         part3 = nums[left-1]*nums[i]*nums[right]
    #         mini = min(part1+part2+part3,mini)
    #     dp[left][right] = mini
    #     return mini
    # return helper(1,len(nums)-1)

nums =  [10, 15, 20, 25]
print(matrixMultiplication(nums))