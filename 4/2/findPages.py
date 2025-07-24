def allocatedPages(nums,pages):
    student = 1
    allocated_pages = 0
    for i in nums:
        if allocated_pages + i <= pages:
            allocated_pages += i
        else:
            student +=1
            allocated_pages = i
    return student

def findPages(nums,m):
    if len(nums) < m:
        return -1
    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = int((left+right)/2)
        if allocatedPages(nums,mid) > m:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [25, 46, 28, 49, 24]
m = 7
print(findPages(nums,m))