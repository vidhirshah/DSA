def maxProfit(prices:list):
    dp = []
    count = 0
    for i in range(len(prices)):
        dp.append([])
        for j in range(3):
            dp[i].append([])
            for k in range(2):
                dp[i][j].append(0)
    for i in range(2):
        dp[-1][i][1] = prices[-1]
    for currIndex in range(len(prices)-2,-1,-1 ):
        for count in range(1,-1,-1):
            for holdings in range(2):
                if holdings:
                    sell = prices[currIndex] + dp[currIndex+1][count+1][0]
                    notSell = dp[currIndex+1][count][1]
                    profit = max(sell,notSell)
                else:
                        buy = -prices[currIndex] + dp[currIndex+1][count][1]
                        notbuy = dp[currIndex+1][count][0]
                        profit = max(buy,notbuy)
                dp[currIndex][count][holdings] = profit
        print(currIndex,dp[currIndex])
    #     return profit
    return dp[0][0][0]

prices = [1,2,3,4,5]
print(maxProfit(prices))