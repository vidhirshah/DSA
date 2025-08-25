def combinationSum(k,n):
    result = []
    subseaq = []
    def helper(n,i):
        if n < 0:
             return
        if len(subseaq) > k:
             return
        if len(subseaq) == k and n == 0:
            result.append(subseaq[:])
            return 
        if i == 10:
            if n == 0 and len(subseaq)==k:
                    result.append(subseaq[:])
            return 
        subseaq.append(i)
        helper(n-i,i+1)
        subseaq.pop()
        helper(n,i+1)
    helper(n,1)
    return result

k = 9
n = 45
print(combinationSum(k,n))