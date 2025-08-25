def combinationSum(candidates,target):
    result = []
    subseaq = []
    candidates.sort()
    def helper(target,i):
        if target < 0:
             return
        if candidates[i] > target:
            if target == 0:
                    result.append(subseaq[:])
            return 
        if i == len(candidates):
            if target == 0:
                    result.append(subseaq[:])
            return 
        if target == 0:
            result.append(subseaq[:])
            return
        subseaq.append(candidates[i])
        helper(target-candidates[i],i+1)
        while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
             i += 1       
        subseaq.pop()
        helper(target,i+1)
    helper(target,0)
    return result

candidates = [10,1,2,7,6,1,1,5]
target = 8
print(combinationSum(candidates,target))