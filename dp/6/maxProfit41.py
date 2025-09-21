def maxProfit(prices:list,k):
    dp = []
    for i in range(len(prices)):
        dp.append([])
        for j in range(k+1):
            dp[i].append([])
            for holdings in range(2):
                dp[i][j].append(-1)
    def helper(currIndex,count,holdings):
        if count >= k:
            return 0
        if currIndex >= len(prices):
            return 0
        if dp[currIndex][count][holdings] != -1:
            return dp[currIndex][count][holdings]
        profit = 0
        if holdings:
            sell = prices[currIndex] + helper(currIndex+1,count+1,0)
            notSell = helper(currIndex+1,count,1)
            profit = max(sell,notSell)
        else:
            if count < k:
                buy = -prices[currIndex] + helper(currIndex+1,count,1)
                notbuy = helper(currIndex+1,count,0)
                profit = max(buy,notbuy)
        dp[currIndex][count][holdings] = profit
        # print(currIndex,dp[currIndex])
        return profit
    return helper(0,0,0)

prices =[3,2,6,5,0,3]
print(maxProfit(prices,2))

