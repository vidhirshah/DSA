def longestCommonSubsequence( s: str):
    dp = []
    reverse_s = s[len(s)-1::-1]
    for i in range(len(s)+1):
        dp.append([])
        for j in range(len(reverse_s)+1):
            dp[i].append(0)
    for i in range(1,len(s)+1):
        for j in range(1,len(reverse_s)+1):
            if s[i-1] == reverse_s[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1] ,dp[i-1][j])
    return dp[-1][-1]

s1 = "cbd"
s2 = "ace"
print(longestCommonSubsequence(s1))