def isSubsetSum(arr,target):
    dp = []
    length = len(arr)
    for i in range(length):
        dp.append([])
        for j in range(target+1):
            dp[i].append(0)
    for i in range(length):
        dp[i][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1
    for i in dp:
        print(i)
    for index in range(1,length):
        for sum in range(1,target+1):
            if arr[index] == sum:
                dp[index][sum] = dp[index-1][sum -arr[index]] 
            left = 0
            if arr[index] <= sum:
                left = dp[index-1][sum -arr[index]]
            right = dp[index-1][sum]
            dp[index][sum] = left + right
                    # for i in dp:
                    #     print(i)
            # print(index,sum)
            # for i in dp:
            #     print(i)
    return dp[length-1][target]

arr = [2,3,5]
t = 6
# arr = [2,3,5]
# t = 6
print(isSubsetSum(arr,t))