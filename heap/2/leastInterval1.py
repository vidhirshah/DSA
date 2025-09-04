import heapq

def leastInterval(tasks: list[str], n: int):
    freq = [0]*26
    for i in tasks:
        freq[ord(i)-ord('A')] -= 1
    pq = []
    for i in freq:
        if i != 0:
            heapq.heappush(pq,i)
    parts = -pq[0] - 1
    slots = parts*n
    length = len(tasks) + pq[0]
    if slots <= length:
        return len(tasks)
    
    return length

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks,n))