from queue import Queue

class MyStack:

    def __init__(self):
        self.qu = Queue()
        return

    def push(self, x: int) -> None:
        self.qu.put(x)
        for i in range(self.qu.qsize()-1):
            self.qu.put(self.qu.get())
        return

    def pop(self) -> int:
        return self.qu.get()

    def top(self) -> int:
        return self.qu.queue[0]

    def empty(self) -> bool:
        return self.qu.empty()



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2,param_3,param_4)