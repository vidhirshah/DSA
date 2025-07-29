def minPatches(nums, n):
    patches = 0
    miss = 1
    miss <= n
    i = 0
    while miss <= n:
        print(i,miss)
        if i <= len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            # Patch needed
            miss += miss
            patches += 1
    return patches

print(minPatches([1,5,10],20))