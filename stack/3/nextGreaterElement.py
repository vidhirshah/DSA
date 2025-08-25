def nextGreaterElement(nums1: list[int],nums2: list[int]) -> list[int]:
    stack = []
    n = len(nums2)
    ans = [0]*n
    m = len(nums1)
    ans1 = [0]*m
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            ans[i] = -1
        elif stack[-1] > nums2[i]:
            ans[i] = stack[-1]
        else:
            while len(stack) != 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
        stack.append(nums2[i])       
    for i in range(m):
        index = nums2.index(nums1[i])
        ans1[i] = ans[index]
    return ans1

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1,nums2))