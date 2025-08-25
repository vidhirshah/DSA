def subsets(nums):
    n = len(nums)
    ans = []
    for i in range(2**n):
        ans.append([])
        for j in range(n):
            if i & (1<<j):
                ans[-1].append(nums[j])
    return ans

nums = [1,2,3]
print(subsets(nums))