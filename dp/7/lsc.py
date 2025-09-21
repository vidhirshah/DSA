def lengthOfLIS(words:list):
    sorted_wprds = sorted(words,key = len)
    def isPredec(p1,p2):
        if len(sorted_wprds[p1]) == len(sorted_wprds[p2]):
            return False
        if abs(len(sorted_wprds[p1]) - len(sorted_wprds[p2])) != 1:
            return False
        l1 = 0
        l2 = 0
        while l1 < len(sorted_wprds[p1])  and l2 < len(sorted_wprds[p2]):
            if sorted_wprds[p1][l1] == sorted_wprds[p2][l2] :
                l1 += 1
                l2 += 1
            else:
                l2 += 1
        if len(sorted_wprds[p1]) == l1 :
            return True
        return False
    dp = [1]*len(sorted_wprds)
    ans = 0
    for i in range(len(sorted_wprds)):
        for j in range(i):
            if isPredec(j,i):
                dp[i] = max(dp[j]+ 1,dp[i])
        ans = max(ans,dp[i])
    return ans

words = ["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]
print(lengthOfLIS(words))