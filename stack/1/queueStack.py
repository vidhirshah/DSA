class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2,param_4)