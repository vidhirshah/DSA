def subsetSums(nums):
    result = []
    def helper(sum,i):
        if i == len(nums):
            result.append(sum)
            return
        # subseq.append(nums[i])
        helper(sum + nums[i],i+1)
        # subseq.pop()
        helper(sum,i+1)
        return
    helper(0,0)
    return result

nums = [1,2,5]
print(subsetSums(nums))
