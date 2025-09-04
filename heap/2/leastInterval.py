import heapq

def leastInterval(tasks: list[str], n: int):
    freq = [0]*26
    for i in tasks:
        freq[ord(i)-ord('A')] -= 1
    pq = []
    for i in freq:
        if i != 0:
            heapq.heappush(pq,i)
    task_count = 0
    time = 0
    while len(pq) > 0:
        store = []
        cycles = n + 1
        task_count = 0
        while cycles > 0 and len(pq) > 0:
            curr_freq = -heapq.heappop(pq)
            cycles -= 1
            task_count += 1
            if curr_freq > 1:
                store.append(-(curr_freq-1))
        for i in store:
            heapq.heappush(pq,i)
        print(task_count,cycles,time,pq)
        if  pq:
            time += n + 1
            # task_count += n +1
            # print(cycles,task_count)
        else:
            time += task_count 
    return time

tasks = ["A","C","A","B","D","B"]
n = 1
print(leastInterval(tasks,n))