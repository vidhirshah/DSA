def merge(nums1, m: int, nums2, n: int):
    length = m + n
    gap = int((m+n)/2) + length % 2
    while gap > 0:
        left = 0
        right = left + gap
        while right < length:
            if left > m and right <= n:
                if nums2[left] > nums2[right]:
                    nums2[left] , nums2[right] = nums2[right] , nums2[left]
            elif left < m and right < m:
                if nums1[left] > nums1[right]:
                    nums1[left] , nums1[right] = nums1[right] , nums1[left]
            elif left < m and right <= n:
                if nums1[left] > nums2[right - left - 1]:
                    nums1[left] , nums2[right - left - 1] = nums2[right - left - 1] , nums1[left]
            left = left + 1
            right = right + 1
        if gap != 1:
            gap = int(gap/2) + gap % 2
        else:
            break
    for i in range(m,m+n):
        nums1[i] = nums2[i-m]
    return

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print(nums1)