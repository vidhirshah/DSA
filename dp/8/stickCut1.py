def minCost(n,cuts:list):
    sortedCuts = sorted(cuts)
    sortedCuts.insert(0,0)
    sortedCuts.append(n)
    dp = []
    for i in range(len(sortedCuts)):
        dp.append([])
        for j in range(len(sortedCuts)):
            if i > j or i == 0 or i == len(sortedCuts)-1:
                dp[i].append(0)
            else:
                dp[i].append(10e9)
    for left in range(len(sortedCuts)-2,0,-1):
        for right in range(1,len(sortedCuts)-1):
            if left > right:
                continue
            for i in range(left,right+1) :
                part1 = dp[left][ i-1]
                part2 = dp[i+1][right]
                dp[left][right] = min(sortedCuts[right+1] - sortedCuts[left-1] + part1 + part2, dp[left][right])

    return dp[1][len(sortedCuts)-2]

n = 9
cuts = [5,6,1,4,2]

print(minCost(n,cuts))