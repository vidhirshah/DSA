def bin_search(nums,lower,mid,upper,target):
    if lower > upper:
        return -1
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        upper = mid - 1
    else:
        lower = mid + 1
    mid = int((lower+upper)/2)
    return bin_search(nums,lower,mid,upper,target)

def search(nums,target):
    lower = 0
    upper = len(nums) -1
    middle = int((lower+upper)/2)
    return bin_search(nums,lower,middle,upper,target)

nums = [-1,0,3,5,9,12]
print(search(nums,-98))