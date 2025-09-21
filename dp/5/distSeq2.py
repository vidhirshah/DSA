def longestCommonSubsequence( s: str, t: str):
    dp = []
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s + 1):
        dp.append([])
        for j in range(len_t + 1):
            dp[i].append(-1)
    for i in range(len_t+1):
        dp[0][i] = 0
    for i in range(len_s+1):
        dp[i][0] = 1
    for p1 in range(1,len_s+1):
        for p2 in range(1,len_t+1):
            count = 0
            if s[p1-1] == t[p2-1]:
                count  += dp[p1-1][p2-1] +  dp[p1-1][p2]
            else:
                count += dp[p1-1][p2]
            dp[p1][p2] = count
    return dp[-1][-1]
    # def helper(p1,p2):
    #     if p2 < 0:
    #         return 1
    #     if p1 < 0:
    #         return 0
    #     if dp[p1][p2] != -1:
    #         return dp[p1][p2]
    #     count = 0
    #     if s[p1] == t[p2]:
    #         count  = helper(p1-1,p2-1) +  helper(p1-1,p2) 
    #     else:
    #         count += helper(p1-1,p2)
    #     dp[p1][p2] = count
    #     return  count 
    # return helper(len(s)-1,len(t)-1)

s1 = "babgbag"
s2 = "bag"
print(longestCommonSubsequence(s1,s2))