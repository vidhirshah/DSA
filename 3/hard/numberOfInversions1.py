def merge(arr,lower,middle,upper):
    count = 0
    n1 = middle - lower + 1
    n2 = upper - middle 
    arr1 = [0]*(n1) 
    arr2 = [0]*(n2)
    arr1[:] = arr[lower:middle+1]
    arr2[:] = arr[middle+1:upper+1]
    left = 0
    right = 0
    # 2,3,5
    # 1,4
    while left < n1 and right < n2:
        if arr1[left] <= arr2[right]:
            arr[lower] = arr1[left]
            left = left + 1
        else:
            arr[lower] = arr2[right]
            count = count + n1 - left
            right = right + 1
        lower = lower + 1
    if left < n1 :
        while left < n1:
            arr[lower] = arr1[left]
            lower = lower + 1
            left = left + 1
    if right < n2:
        while right < n2:
            arr[lower] = arr2[right]
            lower = lower + 1
            right = right + 1
    return count

def numberOfInversions(nums,lower,upper):
    if lower == upper:
        return 0
    middle = int((lower+upper)/2)
    numberOfInversions(nums,lower,middle)
    numberOfInversions(nums,middle+1,upper)
    counter = merge(nums,lower,middle,upper)
    return counter

nums = [-10, -5, 6, 11, 15, 17]
print(numberOfInversions(nums,0,len(nums)-1))