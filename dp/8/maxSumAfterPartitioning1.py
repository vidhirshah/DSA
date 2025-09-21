def maxSumAfterPartitioning(arr:list,k):
    n = len(arr)
    dp = [0]*(n+1)
    for index in range(n-1,-1,-1):
        maxno = 0
        maxSum = 0
        for i in range(k):
            if index + i< len(arr):
                maxno = max(maxno,arr[index+ i])
                maxSum = max(maxSum,maxno*(i+1)+dp[index+1+i])
        dp[index] = maxSum
    return dp[0]

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioning(arr,k))