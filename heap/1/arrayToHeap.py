def heapify(i,array:list):
    n = len(array)
    while i < int(len(array)/2) + 1:
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right
        if largest == i :
            return
        array[i],array[largest] = array[largest],array[i]
        i = largest
    return

def arrayToheap(array):
    i = 0
    for i in range(int(len(array)/2)+1,-1,-1):
        heapify(i,array)
        print(i,array)
    return

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
arrayToheap(arr)
print(arr)