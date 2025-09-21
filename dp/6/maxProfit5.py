def maxProfit(prices:list):
    def helper(currIndex,holdings):
        if currIndex >= len(prices):
            return 0
        profit = 0
        if holdings:
            sell = prices[currIndex] + helper(currIndex+2,0)
            notSell = helper(currIndex+1,1)
            profit = max(sell,notSell)
        else:
            buy = -prices[currIndex] + helper(currIndex+1,1)
            notbuy = helper(currIndex+1,0)
            profit = max(buy,notbuy)
        return profit
    return helper(0,0,0)

prices =[1]
print(maxProfit(prices))

