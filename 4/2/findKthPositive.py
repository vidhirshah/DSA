def findKthPositive(arr,k):
    count = 0
    for i in range(1,max(arr)+k+1):
        if i not in arr:
            count = count + 1
        if count == k:
            return i
    return -1

arr = [1,2,3,4]
k = 2
print(findKthPositive(arr,k))