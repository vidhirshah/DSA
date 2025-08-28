import collections

class Node:
    def __init__(self,key,val,prev=None,next=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = prev
        self.next = next

class DLL:

    def __init__(self):
        self.head = Node(-1,-1,None,None)
        self.tail = Node(-1,-1,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def deleteNode(self,pointer:Node):
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev
        pointer.next = None
        pointer.prev = None
        self.size -= 1
        return
    
    def insertNode(self,pointer:Node):
        pointer.next = self.head.next
        pointer.prev = self.head
        self.head.next.prev = pointer
        self.head.next = pointer
        self.size += 1
        return

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freqTable = collections.defaultdict(DLL)
        self.cache = {}
        self.minfreq = 0

    def traversl(self):
        for i in self.freqTable:
            print("Frequency",i)
            pointer = self.freqTable[i].head
            while pointer != None:
                if pointer !=self.freqTable[i].head and pointer != self.freqTable[i].tail:
                    print(pointer.key,pointer.val)
                else:
                    print(pointer.val)
                pointer = pointer.next
        return
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ans = self.cache[key]
        retVVal = self.updateCache(ans,key,ans.val)
        # self.traversl()
        return retVVal
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            ans = self.cache[key]
            self.updateCache(ans,key,value)
            return
        if len(self.cache) >= self.capacity:
            temp = self.freqTable[self.minfreq].tail.prev
            self.freqTable[self.minfreq].deleteNode(temp)
            del self.cache[temp.key]
        temp = Node(key,value,None,None)
        self.minfreq = 1
        self.freqTable[1].insertNode(temp)
        self.cache[key] = temp
        # self.traversl()
        return
    
    def updateCache(self,pointer:Node,key:int,value:int):
        prevFreq = pointer.freq
        newFreq = pointer.freq + 1
        pointer.freq = newFreq
        pointer.val = value
        self.freqTable[prevFreq].deleteNode(pointer)
        self.freqTable[newFreq].insertNode(pointer)
        if prevFreq == self.minfreq and self.freqTable[self.minfreq].size == 0:
            self.minfreq = prevFreq + 1
        return value
    

ans = LFUCache(2)
print(ans.put(1,1))
print(ans.put(2,2))
print("get - ",ans.get(1))
print(None)
print(ans.put(3,3))
print("get - ",ans.get(2))
print(None)
print("get - ",ans.get(3))
print(None)
print(ans.put(4,4))
print("get - ",ans.get(1))
print(None)
print("get - ",ans.get(3))
print(None)
print("get - ",ans.get(4))
print(None)
