def longestCommonSubsequence( s: str, t: str):

    def helper(p1,p2):
        if p2 < 0:
            return 1
        if p1 < 0:
            return 0
        count = 0
        if s[p1] == t[p2]:
            count  = helper(p1-1,p2-1) +  helper(p1-1,p2) 
        else:
            count += helper(p1-1,p2)
        return  count 
    return helper(len(s)-1,len(t)-1)

s1 = "babgbag"
s2 = "bag"
print(longestCommonSubsequence(s1,s2))