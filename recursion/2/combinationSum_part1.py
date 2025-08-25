def combinationSum(candidates,target):
    result = []
    subseaq = []
    def helper(sum,i):
        if i == len(candidates):
            if sum == target:
                print(sorted(subseaq[:]))
                if sorted(subseaq[:]) not in result:
                    result.append(sorted(subseaq[:]))
            return 
        sum += candidates[i]
        subseaq.append(candidates[i])
        helper(sum,i+1)
        sum -= candidates[i]
        subseaq.pop()
        helper(sum,i+1)
    helper(0,0)
    return result

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(candidates,target))