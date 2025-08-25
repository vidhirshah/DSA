def partition(s):
    result = []
    ans = []
    def ifPallindrome(x):
        n = len(x)
        for i in range(int(n/2)):
            if x[i] != x[n-1-i]:
                return False
        return True
    n = len(s)
    def ifPartition(ind):
        if ind == len(s)-1:
            result.append(ans[:])
            return 
        for i in range(ind+1,len(s)):
            if ifPallindrome(s[ind+1:i+1]):
                ans.append(s[ind+1:i+1])
                ifPartition(i)
                ans.pop()
        return 
    
    for i in range(n):
        if ifPallindrome(s[:i+1]):
            ans.append(s[:i+1])
            ifPartition(i)
            ans.pop()
    return result

s = "cdd"
print(partition(s))