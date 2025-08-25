class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        if not self.stock :
            self.stock.append([price,1])
            print(self.stock,1)
            return 1
        else:
            span = 1
            while self.stock and self.stock[-1][0] <= price:
                span += self.stock.pop()[1]
            self.stock.append([price,span])
        print(self.stock,span)
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
ans = [[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]
for i in ans:
    param_1 = obj.next(i[0])
    print(i[0],param_1)