class Solution:

    def initializeHeap(self):
        self.heap = []
        return

    def insert(self, key):
        self.heap.append(key)
        i = self.heapSize() -1
        while i > 0:
            parent = int((i-1)/2)
            if self.heap[i] >= self.heap[parent]:
                break
            self.heap[i] , self.heap[parent] = self.heap[parent] , self.heap[i]
            i = parent
        return

    def changeKey(self, index, new_val):
        self.heap[index] , self.heap[-1] = self.heap[-1] , self.heap[index]
        self.heap.pop()
        self.heapify(index)
        self.insert(new_val)
        return
    
    def heapify(self,i):
        n = self.heapSize()
        while i <= int(n/2) + 1:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i
            if left < n and self.heap[left] < self.heap[i]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                # self.heap[right] , self.heap[i] = self.heap[i] , self.heap[right]
            if smallest == i:
                break
            self.heap[smallest] , self.heap[i] = self.heap[i] , self.heap[smallest]
            i = smallest
        return

    def extractMin(self):
        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
        self.heap.pop()
        n = self.heapSize()
        self.heapify(0)
        return

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        return False

    def getMin(self):
        return self.heap[0]

    def heapSize(self):
        return len(self.heap)
    
["extractMin", "changeKey" , "getMin" ]

nums = [ 60,50,40,30,70 ]

heap = Solution()
heap.initializeHeap()
heap.insert(4)
# print(heap.heap)
heap.insert(1)
# print(heap.heap)
heap.insert(10)
# print(heap.heap)
# print(heap.getMin())
# print(heap.heapSize())
# print(heap.isEmpty())
heap.extractMin()
# print(heap.heap)
heap.changeKey(0,16)
print(heap.heap)
print(heap.getMin())

# nums = [60,50,40,30,20,5,70]
# for i in nums:
#     heap.insert(i)
# print(heap.heap)

# heap.extractMin()
# print(heap.heap)