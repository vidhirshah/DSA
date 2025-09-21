def unboundedKnapsack( val:list, N):
    dp = []
    for i in range(len(val)):
        dp.append([])
        for j in range(N+1):
            dp[i].append(-1)
    for i in range(len(val)):
        dp[i][0] = 0
    for i in range(N+1):
        dp[0][i] = val[0]*i
    for i in range(1,len(val)):
        for j in range(0,N+1):
            nottaken = dp[i-1][j]
            taken = 0
            if j - i -1>= 0:
                taken = val[i] + dp[i][j - i -1]
            dp[i][j] = max(taken ,nottaken)
    return dp[len(val)-1][N]

val = [1, 6, 8, 9, 10, 19, 7, 20]
N = 8
val = [1, 5, 8, 9]
N = 4
print(unboundedKnapsack(val,N))