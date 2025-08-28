import heapq

def nearlySorted(arr:list,k):
    pq = []
    # for i in range(k):
    #     heapq.heappush(pq,arr[i])
    index = 0
    for i in range(len(arr)):
        heapq.heappush(pq,arr[i])
        if len(pq) > k:
            arr[index] = pq[0]
            index += 1
            heapq.heappop(pq)
            
    while len(pq) > 0:
        arr[index] = pq[0]
        index += 1
        heapq.heappop(pq)
    return

arr = [6,5,3,2,8,10,9]
nearlySorted(arr,3)
print(arr)