def insertionSort(arr:list,i):
    if i >= len(arr):
        return
    j = i
    while j > 0 and arr[j-1] > a[j]:
        arr[j-1] , arr[j] = arr[j] , arr[j-1]
        j = j -1
    insertionSort(arr,i+1)
    return 

a = [14,9,15,12,6,8,13]
insertionSort(a,1)
print(a)