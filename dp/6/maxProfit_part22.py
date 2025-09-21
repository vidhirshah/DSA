def maxProfit(prices:list):
    dp = []
    for i in range(len(prices)):
        dp.append([])
        for j in range(2):
            dp[i].append(0)
    dp[-1][1] = prices[-1]
    for currIndex in range(len(prices)-2,-1,-1):
        for holdings in range(2):
            profit = 0
            if holdings:
                sell = prices[currIndex] + dp[currIndex+1][0]
                notSell = dp[currIndex+1][1]
                profit = max(sell,notSell)
            else:
                buy = -prices[currIndex] + dp[currIndex+1][1]
                notbuy = dp[currIndex+1][0]
                profit = max(buy,notbuy)
            dp[currIndex][holdings] = profit
    return dp[0][0]

prices = [3,2,6,5,0,3]
print(maxProfit(prices))

