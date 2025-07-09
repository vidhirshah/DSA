def rotate(nums,k):
    length = len(nums)
    temp = nums.copy()
    for i in range(len(temp)):
        nums[(i+k)%length] = temp[i]
    return

n = [1,2,3,4,5,6,7]
k = 3
rotate(n,k)
print(n)