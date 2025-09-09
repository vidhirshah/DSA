def isSubsetSum1(arr,diff):
    total = sum(arr)
    target = total + diff
    target = int(target/2)
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
        for sum1 in range(1,target+1):
            if arr[index] == sum1:
                dp[index][sum1] = dp[index-1][sum1 -arr[index]] 
            left = 0
            if arr[index] <= sum1:
                left = dp[index-1][sum1 -arr[index]]
            right = dp[index-1][sum1]
            dp[index][sum1] = left + right
                    # for i in dp:
                    #     print(i)
            # print(index,sum1)
            # for i in dp:
            #     print(i)
    return dp[length-1][target]

arr = [1, 2, 3,4]
t = 2

# arr = [2,3,5]
# t = 6
print(isSubsetSum1(arr,t))