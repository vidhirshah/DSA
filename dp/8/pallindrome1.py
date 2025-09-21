def minCut(s:str):
    def isPal(left,right):
        mid = int((left+right)/2)
        mid = mid - left +1
        for i in range(mid):
            if s[left+i] != s[right-i]:
                return False
        return True
    dp = []
    for i in range(len(s)+1):
        dp.append(0)
    for left in range(len(s)-1,-1,-1):
        mini = 10e9
        for right in range(left,len(s)):
            if isPal(left,right) == True:
                cost = 1 + dp[right+1] 
                mini = min(mini,cost)
        dp[left] = mini
    return dp[0] -1


s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
print(minCut(s))