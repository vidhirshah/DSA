def merge(arr,lower,middle,upper):
    n1 = middle - lower + 1
    n2 = upper - middle 
    arr1 = [0]*(n1) 
    arr2 = [0]*(n2)
    arr1[:] = arr[lower:middle+1]
    arr2[:] = arr[middle+1:upper+1]
    right = 0
    left = 0
    while left < n1 and right < n2:
        if arr1[left] <= arr2[right]:
            arr[lower] = arr1[left]
            left = left + 1
        else:
            arr[lower] = arr2[right]
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
    return 

def sort(nums,lower,upper):
    if lower == upper:
        return 0
    middle = int((lower+upper)/2)
    i = sort(nums,lower,middle)
    j = sort(nums,middle+1,upper)
    k = 0
    left = lower
    right = middle + 1
    while left < middle + 1 and right < upper+1:
        if nums[left] <= 2*nums[right]:
            left = left + 1
        elif nums[left] > 2*nums[right]:
            while right < upper +1 and nums[left] > 2*nums[right]:
                k = k + middle + 1 -left
                right = right + 1
    counter = merge(nums,lower,middle,upper)
    return i + j + k


def reversePairs(nums):
    return sort(nums,0,len(nums)-1)

nums = [1,2,2,3,3,1]
print(reversePairs(nums))
print(nums)