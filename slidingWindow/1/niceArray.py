def numberOfSubarrays(nums,k):
    count = 0
    for i in range(len(nums)):
        odds = 0
        for j in range(i,len(nums)):
            odds += nums[j]%2
            if odds == k:
                count += 1
            elif odds > k:
                break
    return count

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums,k))