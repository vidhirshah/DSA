def maxProfit(prices:list):
    dp = []
    for i in range(len(prices)):
        dp.append([])
        for j in range(2):
            dp[i].append(-1)
    def helper(currIndex,holdings):
        if currIndex >= len(prices):
            return 0
        if dp[currIndex][holdings] != -1:
            print("a")
            return dp[currIndex][holdings]
        profit = 0
        if holdings:
            sell = prices[currIndex] + helper(currIndex+1,0)
            notSell = helper(currIndex+1,1)
            profit = max(sell,notSell)
        else:
            buy = -prices[currIndex] + helper(currIndex+1,1)
            notbuy = helper(currIndex+1,0)
            profit = max(buy,notbuy)
        dp[currIndex][holdings] = profit
        for i in dp:
            print(i)

        return profit
    return helper(0,0)

prices = [3,2,6,5,0,3]
print(maxProfit(prices))

