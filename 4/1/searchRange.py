def search(nums,target):
    left = 0
    right = len(nums) - 1
    start = -1
    end = -1
    middle = int((left+right)/2)
    while left <= right:
        if nums[middle] < target:
            start = middle
            left = middle + 1
        else:
            right = middle - 1
        middle = int((left+right)/2)
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[middle] <= target:
            left = middle + 1
        else:
            end = middle
            right = middle - 1
        middle = int((left+right)/2)
    if (start == -1 and end == 0 ) or (start == len(nums)-1 and end == -1)or start +1 ==end:
        return[-1,-1]
    if end ==-1 and start == -1:
        return [0,len(nums)-1]
    if end == -1:
        return [start+1,len(nums)-1]
    return [start,end]

nums = [5,7,7,8,8,10]
print(search(nums,6))