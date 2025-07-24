def kthElement(nums1,nums2,k):
    n1 = len(nums1)
    n2 = len(nums2)
    i = 0
    j = 0
    pointer = 0
    while(i < n1 and j < n2):
        if nums1[i] <= nums2[j]:
            if pointer == k - 1:
                return nums1[i]
            i += 1
        else:
            if pointer == k - 1:
                return nums2[j]
            j += 1
        pointer += 1
    while i < n1:
        if pointer == k - 1:
            return nums1[i]
        i += 1
        pointer += 1
    while j < n2:
        if pointer == k - 1:
            return nums2[j]
        j += 1
        pointer += 1
    return -1

# nums1 = [1,3]
# nums2 = [2]
nums1 =  [100, 112, 256, 349, 770]
nums2 = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(kthElement(nums1,nums2,k))