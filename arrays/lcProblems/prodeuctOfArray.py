# Method 1
# def productExceptSelf(nums):
#     count_zeros = 0
#     product = 1
#     output = [0]*len(nums)
#     for i in nums:
#         if i == 0:
#             count_zeros += 1
#         else:
#             product *= i
#     if count_zeros > 1:
#         return output
#     if count_zeros == 1:
#         output[nums.index(0)] = product
#         return output
#     for i in range(len(nums)):
#         output[i] = int(product/nums[i])
#     return output

# Method 1
def productExceptSelf(nums):
    n = len(nums)
    output = [0]*n
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1,-1,-1):
        output[i] *= right
        right *= nums[i]
    return output

nums = [1,2,3,4]
print(productExceptSelf(nums))
