def maxProfit(prices:list):
    profit = 0
    mini = prices[0]
    for i in range(len(prices)):
        profit = max(profit,prices[i]-mini)
        mini = min(mini,prices[i])
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))