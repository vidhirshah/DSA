def search(nums,x):
    left = 0
    right = len(nums) - 1
    floor = -1
    ceil = -1
    middle = int((left+right)/2)
    while left <= right:
        if nums[middle] == x:
            return [nums[middle],nums[middle]]
        if nums[middle] < x:
            floor = nums[middle]
            left = middle + 1
        else:
            ceil = nums[middle]
            right = middle - 1
        middle = int((left+right)/2)
    return [floor,ceil]

nums = [2, 4, 4, 7, 8, 10]
print(search(nums,3))