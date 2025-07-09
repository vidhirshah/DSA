def rotate(nums,k):
    length = len(nums)
    k = k % length
    temp = nums[0:length - k]
    nums[0:k] = nums[length - k:]
    nums[k:] = temp
    return

n = [1,2,3,4,5,6,7]
k = 3
rotate(n,k)
print(n)