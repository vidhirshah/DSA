def bubbleSort(arr:list):
    for i in range(len(arr)-1,0,-1):
        ifswap = 0
        for j in range(1,i+1):
            if arr[j-1] > arr[j]:
                arr[j-1] , arr[j] = arr[j] , arr[j-1]
                ifswap = 1
        if ifswap == 0:
            break
    # for i in range(0,len(arr)-1):
    #     for j in range(0,len(arr)  -i - 1):
    #         if arr[j] > arr[j+1]:
    #             arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return 

a = [5,4,1,2,3]
bubbleSort(a)
print(a)