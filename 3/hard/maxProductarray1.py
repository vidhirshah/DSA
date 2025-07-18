def maxProduct(nums):
    max_product = -2**32
    prefix = 1
    suffix = 1
    for i in range(len(nums)):
        prefix = nums[i] * prefix
        suffix = nums[len(nums)-1-i]*suffix
        max_product = max(prefix,suffix,max_product)
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
    return max_product

nums = [-2,0,-1]
print(maxProduct(nums))