def minCut(s:str):
    def isPal(left,right):
        mid = int((left+right)/2)
        # print(left,mid,right)
        mid = mid - left +1
        for i in range(mid):
            # print(i)
            if s[left+i] != s[right-i]:
                return False
        # print(True)
        return True
    dp = []
    for i in range(len(s)):
        dp.append([])
        for j in range(len(s)):
            dp[i].append(-1)
    def helper(left,right):
        if left > right:
            return 0
        if isPal(left,right):
            return 0
        if dp[left][right] != -1:
            return  dp[left][right]
        mini = 10e9
        for i in range(left,right):
            part1 = helper(left,i)
            part2 = helper(i+1,right)
            mini = min(1+part1+part2,mini)
        dp[left][right] = mini
        return mini
    return helper(0,len(s)-1)

s = "aab"
print(minCut(s))