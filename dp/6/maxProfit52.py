def maxProfit(prices:list):
    if len(prices) <= 1:
        return 0
    dp = []
    for i in range(len(prices)+2):
        dp.append([])
        for j in range(2):
            dp[i].append(0)
    # dp[-1][1] = prices[-1]
    # dp[-2][1] = prices[-2]
    for currIndex in range(len(prices)-1,-1,-1):
        for holdings in range(2):
            profit = 0
            if holdings:
                sell = prices[currIndex] + dp[currIndex+2][0]
                notSell = dp[currIndex+1][1]
                profit = max(sell,notSell)
            else:
                buy = -prices[currIndex] + dp[currIndex+1][1]
                notbuy = dp[currIndex+1][0]
                profit = max(buy,notbuy)
            dp[currIndex][holdings] = profit
    return dp[0][0]

prices = [1,2,3,0,2]
print(maxProfit(prices))

