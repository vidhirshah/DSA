def minPatches(nums, n):
    miss = 1
    i = 0
    patches = 0
    
    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            miss += miss
            patches += 1    
    return patches

print(minPatches([1,5,10],20))