def isSubsetSum(arr,target):
    dp = []
    length = len(arr)
    for i in range(length):
        dp.append([])
        for j in range(target+1):
            dp[i].append(False)
    for i in range(length):
        dp[i][0] = True
    if arr[0] <= target:
        dp[0][arr[0]] = True
    for i in dp:
        print(i)
    for index in range(1,length):
        for sum in range(1,target+1):
            if arr[index] == sum:
                dp[index][sum] = True
            left = False
            if arr[index] <= sum:
                left = dp[index-1][sum -arr[index]]
            right = dp[index-1][sum]
            dp[index][sum] = left or right
                    # for i in dp:
                    #     print(i)
    return dp[length-1][target]

arr = [1,2,7,3]
t = 10
# arr = [2,3,5]
# t = 6
print(isSubsetSum(arr,t))