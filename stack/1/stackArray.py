class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.array = [0]*1000
    
    def push(self,x:int) -> None:
        self.top += 1
        self.array[self.top] = x
        return

    def pop(self) -> int:
        x = self.array[self.top]
        self.top -= 1
        return x
    
    def topmost(self) -> int:
        return self.array[self.top]
    
    def size(self) -> int:
        return self.size
    
st = Stack()
st.push(1)
st.push(2)
st.push(3)

print(st.topmost())
print(st.pop())
print(st.pop())
print(st.topmost())
print(st.pop())
# print(st.topmost())