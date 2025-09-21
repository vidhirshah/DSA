def isMatch(s: str, p: str):
    def isAllStars(index):
        for i in range(index):
            if p[i] != "*":
                return False
        return True
    dp = []
    s_len = len(s)
    p_len = len(p)
    for i in range(s_len+1):
        dp.append([])
        for j in range(p_len+1):
            dp[i].append(-1)
    for i in range(s_len+1):
        dp[i][0] = False
    dp[0][0] = True
    for j in range(1,p_len+1):        
        dp[0][j] = isAllStars(j)
    for i in range(1,s_len+1):
        for j in range(1,p_len+1):
            if p[j-1] == s[i-1] or p[j-1] == "?":
                dp[i][j] = dp[i-1][j-1] and True
            elif p[j-1] == "*":
                dp[i][j] =  (dp[i][j-1] or dp[i-1][j]) and True
            else:
                dp[i][j] = False
    for i in dp:
        print(i)
    return dp[-1][-1]

s = ""
p = "***"

print(isMatch(s,p))