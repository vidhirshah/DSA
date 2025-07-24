def merge(arr,l1,u1,l2,u2):
    n1 = u1 - l1 + 1
    n2 = u2 - l2 + 1
    left = [0]*(n1)
    right = [0]*(n2)
    left[:] = arr[l1:u1+1]
    right[:] = arr[l2:u2+1]
    i = 0
    j = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[l1] = left[i]
            i = i + 1
        else:
            arr[l1] = right[j]
            j = j + 1
        l1 = l1 + 1
    if i < n1 :
        while i < n1:
            arr[l1] = left[i]
            l1 = l1 + 1
            i = i + 1
    if j < n2:
        while j < n2:
            arr[l1] = right[j]
            l1 = l1 + 1
            j = j + 1
    return 

def mergeSort(arr:list,lower,upper):
    if lower == upper:
        return
    l1 = lower
    u1 = int((lower + upper)/2)
    l2 = u1 + 1
    u2 = upper
    mergeSort(arr,l1,u1)
    mergeSort(arr,l2,u2)
    merge(arr,l1,u1,l2,u2)
    return 

a = [46,9,24,52,20,13]
mergeSort(a,0,len(a)-1)
print(a)