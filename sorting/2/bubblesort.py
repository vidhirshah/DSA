def bubbleSort(arr:list,i):
    if i >= len(arr) -1:
        return
    for j in range(0,len(arr)  -i - 1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]    
    return bubbleSort(arr,i+1)

a = [46,9,24,52,20,13]
bubbleSort(a,0)
print(a)