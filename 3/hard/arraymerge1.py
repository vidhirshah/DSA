def merge(nums1, m: int, nums2, n: int):
    left = m - 1
    right = 0
    while(left >= 0 and right < n):
        print(left,right)
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right] , nums1[left]
        else:
            break
        left = left - 1
        right = right + 1
    nums2.sort()
    nums1[:m] = sorted(nums1[:m])
    nums1[m:] = nums2[:]
    return

nums1 = [2]
m = 1
nums2 = [1]
n = 1
merge(nums1,m,nums2,n)
print(nums1)