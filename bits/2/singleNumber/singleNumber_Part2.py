def singleNumber(nums):
    hash = {}
    for i in nums:
        hash[i] = 1 +hash.get(i,0)
    ans = []
    for i in hash.keys():
        if hash[i] == 1:
            ans.append(i)
    return  ans

nums = [1,2,1,3,2,5]
print(singleNumber(nums))