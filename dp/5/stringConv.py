def longestCommonSubsequence( word1: str, word2: str):
    dp = []
    for i in range(len(word1)+1):
        dp.append([])
        for j in range(len(word2)+1):
            dp[i].append(0)
    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1] ,dp[i-1][j])
        
    return len(word1) + len(word2) - 2*dp[-1][-1]

s1 = "abcde"
s2 = "ace"
print(longestCommonSubsequence(s1,s2))