def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1 
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j = j + 1
            elif sum > 0:
                k = k - 1
            elif sum == 0 :
                result.append([nums[i],nums[j],nums[k]])
                j = j + 1
                k = k - 1
                while j < k and nums[j] == nums[j-1] :
                    j = j + 1
                while j < k and nums[k] == nums[k+1] :
                    k = k - 1
    return result

nums = [-2,0,1,1,2]



print(threeSum(nums))