def longestOnes(nums,k):
    left = 0
    right = 0
    flips = 0
    length = len(nums)
    maxlength = 0
    while right < length:
        if nums[right] == 0:
            flips += 1
        if flips <= k:
            maxlength = max(maxlength,right-left )
        else:
            if nums[left] == 0:
                flips -= 1
            left += 1
        right += 1
    maxlength = max(maxlength,right-left )
    return maxlength

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))