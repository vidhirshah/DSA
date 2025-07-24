def unionArray(nums1,nums2):
    union = []
    l1 = len(nums1)
    l2 = len(nums2)
    i = 0
    j = 0
    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            union.append(nums1[i])
            while i < l1 and nums1[i] == union[-1]:
                i = i + 1
            while j < l2 and nums2[j] == union[-1]:
                j = j + 1
        elif nums1[i] < nums2[j]:
            union.append(nums1[i])
            while i < l1 and nums1[i] == union[-1] :
                i = i + 1
        else:
            union.append(nums2[j])
            while j < l2 and nums2[j] == union[-1] :
                j = j + 1
    if i < l1:
        while i < l1:
            if union[-1] != nums1[i]:
                union.append(nums1[i])
            i = i + 1
    if j < l2:
        while j < l2:
            if union[-1] != nums2[j]:
                union.append(nums2[j])
            j = j + 1
    return union

n1 =  [3, 4, 6, 7, 9, 9]
n2 = [1, 5, 7, 8, 8]
print("1 ", n1)
print("2 ", n2)
print(unionArray(n1,n2))