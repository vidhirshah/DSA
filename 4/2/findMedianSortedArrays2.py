def findMedianSortedArrays(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    INT_MIN = -10**6-1
    INT_MAX = 10**6
    if n1 > n2:
        return findMedianSortedArrays(nums2,nums1)
    left = 0
    right = n1
    median1 = int(n/2)
    median2 = median1 + 1
    while left <= right:
        mid1 = int((left+right)/2)
        mid2 = median1 - mid1
        l1 = INT_MIN
        l2 = INT_MIN
        r1 = INT_MAX
        r2 = INT_MAX
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 > 0:
            l1 = nums1[mid1-1]
        if mid2 > 0:
            l2 = nums2[mid2-1]
        print(mid1,mid2)
        print(l1,l2,r1,r2)
        if l2 <= r1 and l1 <= r2:
            if  n%2 == 0:
                return (max(l1,l2)+min(r1,r2))/2
            else:
                return min(r1,r2)
        elif l2 <= r1:
            right = mid1 - 1
        else:
            left = mid1 + 1
    return -1

nums1 = [1,3]
nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))