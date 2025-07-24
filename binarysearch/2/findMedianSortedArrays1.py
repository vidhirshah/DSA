def findMedianSortedArrays(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    mid = int(n/2) 
    el1 = 0
    el2 = 0
    i = 0
    j = 0
    k = 0
    while(i < n1 and j < n2):
        if nums1[i] <= nums2[j]:
            if k == mid -1:
                el1 = nums1[i]
            if k == mid:
                el2 = nums1[i]
            i += 1
        else:
            if k == mid -1:
                el1 = nums2[j]
            if k == mid:
                el2 = nums2[j]
            j += 1
        k += 1
    while i < n1:
        if k == mid -1:
            el1 = nums1[i]
        if k == mid:
            el2 = nums1[i]
        i += 1
        k += 1
    while j < n2:
        if k == mid -1:
            el1 = nums2[j]
        if k == mid:
            el2 = nums2[j]
        j += 1
        k += 1
    if n % 2 == 1:
        return el2
    return (el1+el2)/2

# nums1 = [1,3]
# nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))