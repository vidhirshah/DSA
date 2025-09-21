def minCost(nums:list):
    nums.append(1)
    nums.insert(0,1)
    dp = []
    for i in range(len(nums)):
        dp.append([])
        for j in range(len(nums)):
            dp[i].append(-1)
    def helper(left,right):
        if left > right :
            return 0
        if dp[left][right] != -1:
            return dp[left][right]
        maxi = 0
        for i in range(left,right+1):
            part1 = helper(left,i-1)
            part2 = helper(i+1,right)
            leftBallons = (part1+part2)
            coins = nums[i]*nums[left-1]*nums[right+1]
            maxi = max(maxi, coins + leftBallons)
        dp[left][right] = maxi
        return maxi
    return helper(1,len(nums)-2)

nums = [1,5]
print(minCost(nums))