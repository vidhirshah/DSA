def reverse(arr :list,i:int):
    arr[i] , arr[len(arr) - i - 1] = arr[len(arr) - i - 1] , arr[i]
    if i == int(len(arr)/2) - 1:
        return
    return reverse(arr,i+1)
arr = [1,2,3,4,5]
reverse(arr,0)
print(arr)