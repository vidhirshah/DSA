def unboundedKnapsack(wt:list, val:list, n, W):
    dp = []
    for i in range(len(val)):
        dp.append([])
        for j in range(W):
            dp[i].append(-1)
    def helper(n,weight):
        if n == len(val):
            return 0
        if weight >= W:
            return 0
        if dp[n][weight] != -1:
            return dp[n][weight]
        nottaken = helper(n+1,weight)
        taken = 0
        if weight + wt[n] <= W:
            taken = val[n] + helper(n+1,weight + wt[n])
        dp[n][weight] = max(taken ,nottaken)
        return dp[n][weight]
    return helper(0,0)

val = [10, 40, 50, 70]
wt = [1,3,4,5]
W = 8
print(unboundedKnapsack(wt,val,len(val),W))