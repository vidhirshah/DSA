def longestOnes(nums,k):
    left = 0
    right = 0
    flips = 0
    index = []
    length = len(nums)
    maxlength = 0
    while right < length:
        if nums[right] == 1:
            maxlength = max(maxlength,right-left+1)
            # right += 1
            # print(maxlength)
        if nums[right] == 0:
            index.append(right)
            if flips < k:
                flips += 1
                maxlength = max(maxlength,right-left + 1)
                # right += 1
            else:
                # print("A")
                left = index.pop(0) + 1
        # print(left,right,maxlength)
        right += 1
    maxlength = max(maxlength,right-left )
    return maxlength

nums = [0,0,0,1]
k = 3
print(longestOnes(nums,k))