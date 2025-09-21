def unboundedKnapsack(wt:list, val:list, n, W):
    dp = []
    for i in range(len(val)):
        dp.append([])
        for j in range(W+1):
            dp[i].append(-1)
    for i in range(len(val)):
        dp[i][0] = 0
    for i in range(W+1):
        div = int(i/wt[0])
        dp[0][div] = val[0]*div
    for i in dp:
        print(i)
    for i in range(1,len(val)):
        for j in range(0,W+1):
            nottaken = dp[i-1][j]
            taken = 0
            if j - wt[i] >= 0:
                taken = val[i] + dp[i][j - wt[i]]
            dp[i][j] = max(taken ,nottaken)
    return dp[len(val)-1][W]

val = [10, 40, 50, 70]
wt = [1,3,4,5]
W = 8
print(unboundedKnapsack(wt,val,len(val),W))