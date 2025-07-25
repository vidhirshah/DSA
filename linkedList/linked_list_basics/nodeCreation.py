class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

x = Node(3)
print(x)
y = x
print(y.data)