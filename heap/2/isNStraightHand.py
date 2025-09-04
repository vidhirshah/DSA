import heapq

def isNStraightHand(hand:list,groupSize):
    if len(hand) % groupSize != 0:
        return False
    pq = []
    for i in hand:
        heapq.heappush(pq,i)
    ans = []
    while len(pq) > 0:
        count = groupSize
        store = []
        ans = []
        while count > 0 and len(pq) > 0:
            # print(ans,pq)
            if not ans:
                ans.append(heapq.heappop(pq))
                count -= 1
                continue
            elif ans[-1] == pq[0]:
                # print("a")
                while pq and ans[-1] == pq[0]:
                    store.append(heapq.heappop(pq))
            if len(ans) >= 1 and pq and ans[-1] + 1 == pq[0]:
                ans.append(heapq.heappop(pq))
            else:
                return False
            count -= 1
            # print(ans,count)
        for i in store:
            heapq.heappush(pq,i)
    return True

hand = [1,1,2,2,3,3]
group = 2
print(isNStraightHand(hand,group))