def isSubsetSum1(nums,target):
    total = sum(nums)
    if target > total:
        return 0
    target1 = total + target
    if target1%2 == 1 or target1 < 0:
        return 0
    target1 = int(target1/2)
    dp = []
    length = len(nums)
    for i in range(length):
        dp.append([])
        for j in range(target1+1):
            dp[i].append(0)
    for i in range(len(nums)):
        if nums[0] == 0:
            dp[i][0] = 2  # 2 cases - pick and not pick
        else:
            dp[i][0] = 1  # 1 case - not pick
    if nums[0] != 0 and nums[0] <= target1:
        dp[0][nums[0]] = 1  
    
    for index in range(1,length):
        for sum1 in range(0,target1+1):
            right = dp[index-1][sum1]
            left = 0
            if nums[index] <= sum1:
                left = dp[index-1][sum1 -nums[index]]
            dp[index][sum1] = left + right 
    for i in dp:
        print(i)
    return dp[length-1][target1]

nums = [1,1,1,1]
t = -1000

# nums = [2,3,5]
# t = 6
print(isSubsetSum1(nums,t))