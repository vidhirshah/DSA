def longestOnes(nums,k):
    left = 0
    right = 0
    flips = 0
    length = len(nums)
    maxlength = 0
    while right < length:
        if nums[right] == 1:
            maxlength = max(maxlength,right-left+1)
            # right += 1
            # print(maxlength)
        if nums[right] == 0:
            if flips < k:
                flips += 1
                maxlength = max(maxlength,right-left + 1)
            else:
                while nums[left] != 0:
                    left += 1
                left += 1
        right += 1
    maxlength = max(maxlength,right-left )
    return maxlength

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))