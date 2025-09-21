def longestCommonSubsequence( text1: str, text2: str):
    dp = []
    for i in range(len(text1)+1):
        dp.append([])
        for j in range(len(text2)+1):
            dp[i].append(0)
    for i in range(1,len(text1)+1):
        for j in range(1,len(text2)+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1] ,dp[i-1][j])
    ans = ""
    i = len(text1)
    j = len(text2)
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            ans = text1[i-1] + ans
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i][j-1]:
                j -= 1
            else:
                i -= 1
    return ans

s1 = "abcde"
s2 = "ace"
print(longestCommonSubsequence(s1,s2))