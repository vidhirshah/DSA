def merge(arr,lower,middle,upper):
    n1 = middle - lower + 1
    n2 = upper - middle 
    left = [0]*(n1)
    right = [0]*(n2)
    left[:] = arr[lower:middle+1]
    right[:] = arr[middle+1:upper+1]
    i = 0
    j = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[lower] = left[i]
            i = i + 1
        else:
            arr[lower] = right[j]
            j = j + 1
        lower = lower + 1
    if i < n1 :
        while i < n1:
            arr[lower] = left[i]
            lower = lower + 1
            i = i + 1
    if j < n2:
        while j < n2:
            arr[lower] = right[j]
            lower = lower + 1
            j = j + 1
    return 

def mergeSort(arr:list,lower,upper):
    if lower == upper:
        return
    middle = int((lower + upper)/2)
    mergeSort(arr,lower,middle)
    mergeSort(arr,middle+1,upper)
    merge(arr,lower,middle,upper)
    return 

a = [46,9,24,52,20,13]
mergeSort(a,0,len(a)-1)
print(a)