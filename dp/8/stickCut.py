def minCost(n,cuts:list):
    sortedCuts = sorted(cuts)
    sortedCuts.insert(0,0)
    sortedCuts.append(n)
    dp = []
    for i in range(len(cuts)+2):
        dp.append([])
        for j in range(len(cuts)+2):
            dp[i].append(-1)
    def helper(left,right):
        if left > right :
            return 0
        if dp[left][right] != -1:
            return dp[left][right]
        mini = 10e9
        for i in range(left,right+1):
            part1 = helper(left , i-1)
            part2 = helper(i+1,right)
            mini = min(sortedCuts[right+1] - sortedCuts[left-1] + part1 + part2,mini)
        dp[left][right] = mini
        return mini
    return helper(1,len(sortedCuts)-2)

n = 9
cuts = [5,6,1,4,2]
print(minCost(n,cuts))