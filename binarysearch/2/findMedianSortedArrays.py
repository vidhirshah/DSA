def findMedianSortedArrays(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    temp_array = [0]*n
    i = 0
    j = 0
    k = 0
    while(i < n1 and j < n2):
        if nums1[i] <= nums2[j]:
            temp_array[k] = nums1[i]
            i += 1
        else:
            temp_array[k] = nums2[j]
            j += 1
        k += 1
    while i < n1:
        temp_array[k] = nums1[i]
        i += 1
        k += 1
    while j < n2:
        temp_array[k] = nums2[j]
        j += 1
        k += 1
    if n % 2 == 0:
        half = int(n/2)
        return (temp_array[half-1]+temp_array[half])/2
    return temp_array[int(n/2)]

nums1 = [1,3]
nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))