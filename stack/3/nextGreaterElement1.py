def nextGreaterElement(nums: list[int]) -> list[int]:
    stack = []
    n = len(nums)
    ans = [0]*n
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            ans[i] = -1
        elif stack[-1] > nums[i]:
            ans[i] = stack[-1]
        else:
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
        stack.append(nums[i])     
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            ans[i] = -1
        elif stack[-1] > nums[i]:
            ans[i] = stack[-1]
        else:
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
        stack.append(nums[i])     
    return ans  
nums = [1,4,3,6,3]

print(nextGreaterElement(nums))