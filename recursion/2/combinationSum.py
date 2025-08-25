def combinationSum(candidates,target):
    result = []
    subseaq = []
    def helper(sum,i):
        if i == len(candidates):
            if sum == target:
                result.append((subseaq[:]))
            return 
        count = 0
        while sum <= target:
            count += 1
            sum += candidates[i]
            subseaq.append(candidates[i])
            helper(sum,i+1)
        while count > 0:
            count -= 1
            sum -= candidates[i]
            subseaq.pop()
        helper(sum,i+1)
    helper(0,0)
    return result

candidates = [2,3,5]
target = 13
print(combinationSum(candidates,target))