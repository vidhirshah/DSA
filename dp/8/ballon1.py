def minCost(nums:list):
    nums.append(1)
    nums.insert(0,1)
    dp = []
    for i in range(len(nums)):
        dp.append([])
        for j in range(len(nums)):
            dp[i].append(0)
    for left in range(len(nums)-2,0,-1):
        for right in range(1,len(nums)-1):
            maxi = 0
            for i in range(left,right+1):
                part1 = dp[left][i-1]
                part2 = dp[i+1][right]
                leftBallons = (part1+part2)
                coins = nums[i]*nums[left-1]*nums[right+1]
                maxi = max(maxi, coins + leftBallons)
            dp[left][right] = maxi
    return dp[1][len(nums)-2]

nums = [3,1,5,8]
print(minCost(nums))