def merge(nums1, m: int, nums2, n: int):
    result = [0]*(m+n)
    i = 0
    j = 0
    k = 0
    while(i < m and j < n):
        if nums1[i] <= nums2[j]:
            result[k] = nums1[i]
            i = i + 1
        else:
            result[k] = nums2[j]
            j = j + 1
        k = k + 1
    while i < m:
        result[k] = nums1[i]
        i = i + 1
        k = k + 1
    while j < n:
        result[k] = nums2[j]
        j = j + 1
        k = k + 1
    for i in range(m+n):
        nums1[i] = result[i]
    return

nums1 = [2]
m = 1
nums2 = [1]
n = 1
merge(nums1,m,nums2,n)
print(nums1)