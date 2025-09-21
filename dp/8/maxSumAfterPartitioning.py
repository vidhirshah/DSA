def maxSumAfterPartitioning(arr:list,k):
    dp = [-1]*len(arr)
    def helper(index):
        if index >= len(arr):
            return 0
        if dp[index] != -1:
            return dp[index]
        maxno = 0
        maxSum = 0
        for i in range(k):
            if index + i< len(arr):
                maxno = max(maxno,arr[index+ i])
                maxSum = max(maxSum,maxno*(i+1)+helper(index+1+i))
        dp[index] = maxSum
        return maxSum
    return helper(0)

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioning(arr,k))