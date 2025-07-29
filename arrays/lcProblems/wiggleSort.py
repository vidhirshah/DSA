def wiggleSort(nums):
    sort = sorted(nums) 
    n = len(nums)
    mid = int((n-1)/2)
    nums[::2],nums[1::2] = sort[mid::-1] , sort[:mid:-1]
    return

nums = [1,1,2,2,2,3,3,3]
wiggleSort(nums)
print(nums)