def maxProfit(prices:list):
    dp = []
    count = 0
    for i in range(len(prices)):
        dp.append([])
        for j in range(3):
            dp[i].append([])
            for k in range(2):
                dp[i][j].append(-1)
    def helper(currIndex,count,holdings):
        if count >= 2:
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
            if count < 2:
                buy = -prices[currIndex] + helper(currIndex+1,count,1)
                notbuy = helper(currIndex+1,count,0)
                profit = max(buy,notbuy)
        dp[currIndex][count][holdings] = profit
        print(currIndex,dp[currIndex])
        return profit
    return helper(0,0,0)

prices = [3,3,5,0,0,3,1,4]

print(maxProfit(prices))

