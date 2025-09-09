def isSubsetSum(arr,target):
    dp = []
    for i in range(len(arr)):
        dp.append([])
        for j in range(target+1):
            dp[i].append(-1)
    def helper(index,sum):
        if sum == 0 or arr[index] == sum:
            dp[index][sum] = True
            return True
        if index == len(arr) - 1:
            return False
        if dp[index][sum] != -1:
            return dp[index][sum]
        left = False
        if arr[index] <= sum:
            left = helper(index+1,sum-arr[index]) 
        right = helper(index+1,sum)
        dp[index][sum] = left or right
        return dp[index][sum]
    return helper(0,target)

arr = [1,2,7,3]
t = 10
arr = [2,1,5]
t = 5
print(isSubsetSum(arr,t))