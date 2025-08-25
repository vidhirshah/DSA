class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = 2**31

    def push(self, val: int) -> None:
        if self.minimum > val:
            self.minimum = val
        self.stack.append((val,self.minimum))
        return

    def pop(self) -> None:
        x = self.stack.pop()
        if len(self.stack) > 0:
            self.minimum = self.stack[-1][1]
        else:
            self.minimum = 2**31
        return x[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)
