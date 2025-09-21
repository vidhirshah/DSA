def maxProfit(prices:list,fee):
    def helper(currIndex,holdings):
        if currIndex >= len(prices):
            return 0
        profit = 0
        if holdings:
            sell = prices[currIndex] + helper(currIndex+1,0) -fee
            notSell = helper(currIndex+1,1)
            profit = max(sell,notSell)
        else:
            buy = -prices[currIndex] + helper(currIndex+1,1)
            notbuy = helper(currIndex+1,0)
            profit = max(buy,notbuy)
        return profit
    return helper(0,0)

prices = [1,3,2,8,4,9]
fee = 2
print(maxProfit(prices,fee))

