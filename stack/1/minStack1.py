class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = 2**31

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minimum = val
            self.stack.append(val)
        else:
            if val > self.minimum:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.minimum)
                self.minimum = val
        return

    def pop(self) -> None:
        x = self.stack.pop()
        if self.minimum > x:
            val = self.minimum
            self.minimum = 2*val - x
        else:
            val = x
        return val

    def top(self) -> int:
        if self.minimum > self.stack[-1]:
            val = self.minimum
            self.minimum = 2*val - self.stack[-1]
        else:
            val = self.stack[-1]
        return val

    def getMin(self) -> int:            
        return self.minimum


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
