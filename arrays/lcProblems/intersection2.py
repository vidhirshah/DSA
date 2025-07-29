# Method 1
# def intersection(nums1,nums2):
#     set_nums1 = set(nums1)
#     set_nums2 = set(nums2)
#     res = []
#     for i in set_nums1:
#         if i in set_nums2:
#             res.append(i)
#     return res

def intersection(nums1,nums2):
    res = []
    nums1.sort()
    nums2.sort()
    print(nums1,nums2)
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        print(i,nums1[i],j,nums2[j],res)
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j] :
            i += 1
        else:
            j += 1 
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1,nums2))