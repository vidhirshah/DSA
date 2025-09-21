def unboundedKnapsack(val:list, N):
    dp = []
    for i in range(len(val)):
        dp.append([])
        for j in range(N+1):
            dp[i].append(-1)
    def helper(n,cuts):
        if n >= N:
            return 0
        if cuts >= N:
            return 0
        if dp[n][cuts] != -1:
            return dp[n][cuts]
        nottaken = helper(n+1,cuts)
        taken = 0
        if cuts + n +1<= N:
            taken = val[n] + helper(n,cuts + n + 1)
        dp[n][cuts] = max(taken ,nottaken)
        return dp[n][cuts]
    return helper(0,0)

val = [1, 6, 8, 9, 10, 19, 7, 20]
N = 8
val = [1, 5, 8, 9]
N = 4
print(unboundedKnapsack(val,N))