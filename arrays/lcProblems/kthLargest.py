# Method 1
# def kthLargest(nums,k):
#     return sorted(nums)[len(nums)-k]

# Method 2
# import heapq
# def kthLargest(nums,k):
#     min_heap = []
#     for i in nums:
#         heapq.heappush(min_heap,i)
#         if len(min_heap) > k:
#             heapq.heappop(min_heap)
#     return min_heap[0]

# Method 3
# def kthLargest(nums,k):
#     minimum = min(nums)
#     maximum = max(nums)
#     freq = [0]*(maximum-minimum+1)
#     for i in nums:
#         freq[i-minimum] += 1
#     print(freq)
#     for i in range(len(freq)-1,-1,-1):
#         k -= freq[i]
#         if k <= 0:
#             return i + minimum
#     return -1

# Method 4

def kthLargest(nums,k):
    k = len(nums) - k
    def quickSelect(left,right):
        low = left
        high = right
        pivot = nums[right]
        while low <= high:
            while low <= high and nums[low] < pivot:
                low += 1
            while low <= high and nums[high] > pivot:
                high -= 1
            if low <= high:
                nums[low] , nums[high] = nums[high] , nums[low]
                low += 1
                high -= 1
        if k <= high:
            return quickSelect(left,high)
        elif k >= low:
            return quickSelect(low,right)
        else:
            return nums[k]

    return quickSelect(0,len(nums)-1)

nums = [1]
k = 1
print(kthLargest(nums,k))