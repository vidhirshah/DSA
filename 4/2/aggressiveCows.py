def ifPlaced(nums,k,distance):
    count = 1
    last = 0
    for j in range(1,len(nums)):
        if nums[j] - nums[last] >= distance:
            count +=1
            last = j
        if count == k:
            return True
    return False


def aggressiveCows(nums,k):
    nums.sort()
    max_dis = 0
    for i in range(1,max(nums)-min(nums)+1):
        if ifPlaced(nums,k,i):
            continue
        else:
            return i - 1
    return -1

nums = [0, 3, 4, 7, 9, 10]
k = 4
print(aggressiveCows(nums,k))
