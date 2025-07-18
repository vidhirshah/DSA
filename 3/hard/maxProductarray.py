def maxProduct(nums):
    max_product = 0
    for i in range(len(nums)-1):
        product = nums[i]
        for j in range(i+1,len(nums)):
            product = product*nums[j]
            if product > max_product:
                max_product = product
    return max_product

nums = [2,3,-2,4]
print(maxProduct(nums))