def fourSum(nums,target):
    result = []
    nums = sorted(nums)
    n = len(nums)
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            required = target - nums[i] - nums[j]
            while k < l:
                sum = nums[k] + nums[l]
                if sum < required:
                    k = k + 1
                elif sum > required:
                    l = l - 1
                else:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k = k + 1
                    l = l - 1
                    while k < l and nums[k-1] == nums[k]:
                        k = k + 1
                    while k < l and nums[l+1] == nums[l]:
                        l = l - 1
    return result

nums = [1,0,-1,0,-2,2]
print(fourSum(nums,0))