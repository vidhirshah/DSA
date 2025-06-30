def mergeSort(arr:list):
    for i in range(len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min] , arr[i] = arr[i] , arr[min]
    return 

a = [9,46,24,52,20,13]
mergeSort(a)
print(a)