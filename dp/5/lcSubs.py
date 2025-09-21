def longestCommonSubsequence( text1: str, text2: str):
    dp = []
    for i in range(len(text1)+1):
        dp.append([])
        for j in range(len(text2)+1):
            dp[i].append(0)
    maxi = 0
    for i in range(1,len(text1)+1):
        for j in range(1,len(text2)+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = 0
            maxi = max(maxi,dp[i][j])
    return maxi

s1 = "abcdxyz"
s2 = "xabcdyz"
print(longestCommonSubsequence(s1,s2))