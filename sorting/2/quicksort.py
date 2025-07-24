def quickSort(arr:list,lower,upper):
    if lower >= upper:
        return
    pivot = arr[lower]
    i = lower + 1
    j = upper
    while i < j:
        while i <= upper and arr[i] < pivot :
            i = i + 1
        while j > lower and arr[j] > pivot :
            j = j - 1
        if i < j :  
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
            j = j - 1
    partition = j
    arr[lower] , arr[partition] = arr[partition] , arr[lower]
    quickSort(arr,lower,partition-1)
    quickSort(arr,partition+1,upper)
    return 

a = [20,9,24,52,46,13]
quickSort(a,0,len(a)-1)
print(a)