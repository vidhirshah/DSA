class LRUCache:

    class Node:
        def __init__(self,key,val,prev=None,next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-5,-1)
        self.tail = self.Node(-4,-1,self.head)
        self.head.next = self.tail
        self.map = {}
        self.length = 0

    def deleteNode(self,pointer:Node):
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev
        pointer.next = None
        pointer.prev = None
        return
    
    def insertNode(self,pointer:Node):
        pointer.next = self.head.next
        pointer.prev = self.head
        self.head.next.prev = pointer
        self.head.next = pointer
        return
    
    def traversl(self):
        pointer = self.head
        while pointer != None:
            if pointer !=self.head and pointer != self.tail:
                print(pointer.key,pointer.val)
            else:
                print(pointer.val)
            pointer = pointer.next
        return
    
    def get(self, key: int) -> int:
        value = self.map.get(key,-1)
        if value == -1:
            return -1
        self.deleteNode(value)
        self.insertNode(value)
        self.traversl()
        return value.val
    
    def put(self, key: int, value: int) -> None:
        temp = self.map.get(key,-1)
        print("temp",key,value,temp)
        if temp != -1:
            temp.val = value
            self.deleteNode(temp)
            self.insertNode(temp)
            self.traversl()
            return
        if self.length >= self.capacity :
            self.length -= 1
            self.map.pop(self.tail.prev.key)
            self.deleteNode(self.tail.prev)
        pointer = self.Node(key,value,None,None)
        self.map[key] = pointer
        self.insertNode(pointer)
        self.length += 1
        self.traversl()
        return

["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
ans = LRUCache(2)
print(ans.put(2,1))
print(ans.put(2,2))
print(ans.get(1))
print(None)