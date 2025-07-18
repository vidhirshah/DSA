def search(nums,x):
    left = 0
    right = len(nums) - 1
    index = len(nums)
    middle = int((left+right)/2)
    while left <= right:
        if nums[middle] <= x:
            left = middle + 1
        else:
            index = min(middle,index)
            right = middle - 1
        middle = int((left+right)/2)
    return index

nums = [3,5,8,15,19]
print(search(nums,9))