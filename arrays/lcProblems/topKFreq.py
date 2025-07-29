#  Method 1
# import heapq
# def topKFrequent(nums,k):
#     min_heap = []
#     counter = {}
#     for i in nums:
#         counter[i] = 1 + counter.get(i,0)
#     for i in counter.keys():
#         heapq.heappush(min_heap,(counter[i],i))
#         if len(min_heap) > k:
#             heapq.heappop(min_heap)
#     result = []
#     for i in range(len(min_heap)-1,-1,-1):
#         result.append(heapq.heappop(min_heap)[1])
#     return result

# Method 2
def topKFrequent(nums,k):
    minimum = min(nums)
    maximum = max(nums)
    counter = {}
    for i in nums:
        counter[i] = 1 + counter.get(i,0)
    freq = []
    for i in range(max(counter.values())+1):
        freq.append([])
    for i , f in counter.items():
        freq[f].append(i)
    res = []
    for i in range(len(freq)-1,-1,-1):
        for j in freq[i]:
            res.append(j)
            if len(res) == k:
                return res
    return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))