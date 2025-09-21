def longestCommonSubsequence( word1: str, word2: str):
    dp = []
    len1 = len(word1)
    len2 = len(word2)
    for i in range(len1 + 1):
        dp.append([])
        for j in range(len2 + 1):
            dp[i].append(-1)
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    for p1 in range(1,len1 + 1):
        for p2 in range(1,len2+1):
            if word1[p1-1] == word2[p2-1]:
                dp[p1][p2] =  dp[p1-1][p2-1]
            else:
                dp[p1][p2] =  1 + min(dp[p1-1][p2-1],dp[p1][p2-1],dp[p1-1][p2])
    return dp[-1][-1]

s1 = "horse"
s2 = "ros"
print(longestCommonSubsequence(s1,s2))