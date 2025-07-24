def findMaxConsecutiveOnes(nums):
    max_ones = 0
    temp_max = 0
    for i in nums:
        if i:
            temp_max = temp_max + 1
        else:
            max_ones = max(temp_max,max_ones)
            temp_max = 0
    max_ones = max(temp_max,max_ones)
    return max_ones

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))