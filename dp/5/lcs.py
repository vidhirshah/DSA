def longestCommonSubsequence( text1: str, text2: str):
    dp = []
    for i in range(len(text1)):
        dp.append([])
        for j in range(len(text2)):
            dp[i].append(-1)
    def helper(p1,p2):
        if p1 < 0 or p2 < 0:
            return 0
        if dp[p1][p2] != -1:
            return dp[p1][p2]
        if text1[p1] == text2[p2]:
            dp[p1][p2] = 1 + helper(p1-1,p2-1)
            return dp[p1][p2]
        dp[p1][p2] = max(helper(p1,p2-1) , helper(p1-1,p2))
        return  dp[p1][p2]
    return helper(len(text1)-1,len(text2)-1)

s1 = "abcde"
s2 = "ace"
print(longestCommonSubsequence(s1,s2))