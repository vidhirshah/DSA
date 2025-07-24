def unionArray(nums1,nums2):
    return list(set(nums1 + nums2))

n1 =  [3, 4, 6, 7, 9, 9]
n2 = [1, 5, 7, 8, 8]
print("1 ", n1)
print("2 ", n2)
print(unionArray(n1,n2))