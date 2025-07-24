def search(nums,target):
    left = 0
    right = len(nums) - 1
    middle = int((left+right)/2)
    while left <= right:
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        middle = int((left+right)/2)
    return -1

nums = [-1,0,3,5,9,12]
print(search(nums,13))