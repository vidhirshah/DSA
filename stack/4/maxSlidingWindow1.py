def maxSlidingWindow(nums :list[int],k):
    n = len(nums)
    if n == 1 or k == 1:
        return nums
    ans = []
    queue = []
    for i in range(0,n):
        if len(queue) > 0 and queue[0] < i - k +1:
            queue.pop(0)
        # print(queue,nums[i])
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)
        ans.append(nums[queue[0]])
        # print(ans)
    return ans[k-1:]

nums = [1,3,1,2,0,5]
k = 3
print(nums)
print(maxSlidingWindow(nums,k))