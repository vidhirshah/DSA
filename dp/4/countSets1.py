def isSubsetSum(arr,target):
    dp = []
    for i in range(len(arr)):
        dp.append([])
        for j in range(target+1):
            dp[i].append(-1)
    def helper(index,sum):
        if sum == 0 or arr[index] == sum:
            dp[index][sum] =  1
            return  1
        if index == len(arr) - 1:
            return 0
        if dp[index][sum] != -1:
            return dp[index][sum]
        left = 0
        if arr[index] <= sum:
            left = helper(index+1,sum-arr[index]) 
        right = helper(index+1,sum)
        dp[index][sum] = left + right
        return dp[index][sum]
    return helper(0,target)

arr = [2,3,5]
t = 6
print(isSubsetSum(arr,t))