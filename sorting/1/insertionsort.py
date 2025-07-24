def insertionSort(arr:list):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j-1] > a[j]:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j = j -1
    return 

a = [14,9,15,12,6,8,13]
insertionSort(a)
print(a)