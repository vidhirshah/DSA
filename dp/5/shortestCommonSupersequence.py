def shortestCommonSupersequence( str1: str, str2: str):
    dp = []
    for i in range(len(str1)+1):
        dp.append([])
        for j in range(len(str2)+1):
            dp[i].append(0)
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1] ,dp[i-1][j])
    lcs = ""
    i = len(str1)
    j = len(str2)
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i][j-1]:
                j -= 1
            else:
                i -= 1
    # print(lcs)
    i = 0
    j = 0
    k = 0
    ans = ""
    while j < len(str2):
        if k < len(lcs) and str2[j] == lcs[k]:
            j += 1
            while i < len(str1) and str1[i] !=lcs[k]:
                ans += str1[i]
                i += 1
                if str1[i] == lcs[k]:
                    break
            ans += str1[i]
            i += 1
            k += 1
        else:
            ans += str2[j]
            j += 1
        print(ans,i,j,k,str2[:j+1])
    while i < len(str1):
        ans += str1[i]
        i += 1
    return ans

s1 = "bbbaaaba"
s2 = "bbababbb"
print(shortestCommonSupersequence(s1,s2))