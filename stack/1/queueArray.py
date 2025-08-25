class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.length = 10
        self.array = [0]*self.length
    
    def push(self,x:int) -> None:
        if self.start == -1 and self.end == -1:
            self.start += 1
            self.end += 1
        elif self.start <= self.end and self.end < self.length-1:
            self.end += 1
        elif self.start > self.end :
            if self.start > self.end +1:
                self.end += 1
        self.end %= self.length
        self.array[self.end] = x
        return

    def pop(self) -> int:
        x = self.array[self.end]
        if self.end == self.start:
            self.end = -1
            self.start = -1
        else:
            self.end += 1
            self.end %= self.length
        return x
    
    def topmost(self) -> int:
        return self.array[self.start]
    
    def size(self) -> int:
        return self.length
    
st = Queue()
st.push(1)
st.push(2)
st.push(3)

print(st.size())
# print(st.pop())
# print(st.pop())
# print(st.topmost())
# print(st.pop())
# print(st.topmost())