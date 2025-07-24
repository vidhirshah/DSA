def findKthPositive(arr,k):
    if k < arr[0]:
        return k
    length = len(arr)
    missingels = arr[length-1] - length
    if k > missingels:
        return arr[length-1] + k - missingels
    k = k - arr[0] + 1
    left = 0
    right = length -1
    count = 0
    while left < right-1:
        count +=1
        mid = int((left+right)/2)
        n = mid - left + 1
        range_array = arr[mid] - arr[left] + 1
        missingels = range_array - n
        if k == 0 and missingels == 0:
            left = mid
        if k < missingels:
            right = mid 
        elif k > missingels:
            k -= missingels
            left = mid  
        elif k == missingels:
            right = mid 
        
    return arr[left] + k

arr = [8,11,16,20,29,30,32,33,37,39,42,44,46,47,48,50,52,56,60,63,64,65,68,70,72,74,80]
k = 45
print(arr)
print(findKthPositive(arr,k))