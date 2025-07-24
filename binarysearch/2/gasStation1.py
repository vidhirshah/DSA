import heapq

def minimiseMaxDistance(arr,k):
    n = len(arr)
    distance = [0]*(n-1)
    pq = []
    for i in range(n-1):
        heapq.heappush(pq,((-1)*(arr[i+1] - arr[i])/(distance[i] + 1),i))
    for stations in range(k):
        max_ind = heapq.heappop(pq)[1]
        distance[max_ind] += 1
        heapq.heappush(pq,((-1)*(arr[max_ind+1] - arr[max_ind])/(distance[max_ind] + 1),max_ind))
    return (-1)*heapq.heappop(pq)[0]

arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 1
print(minimiseMaxDistance(arr,k))