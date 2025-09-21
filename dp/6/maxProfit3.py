def maxProfit(prices:list):
    def helper(currIndex,holdings,count):
        if currIndex >= len(prices):
            return 0
        profit = 0
        if holdings:
            sell = prices[currIndex] + helper(currIndex+1,0,count + 1)
            notSell = helper(currIndex+1,1,count)
            profit = max(sell,notSell)
        else:
            if count < 2:
                buy = -prices[currIndex] + helper(currIndex+1,1,count)
                notbuy = helper(currIndex+1,0,count)
                profit = max(buy,notbuy)
        return profit
    return helper(0,0,0)

prices =[7,6,4,3,1]
print(maxProfit(prices))

