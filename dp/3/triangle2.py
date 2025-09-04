def minimumTotal(triangle: list[list[int]]):
    INT_MAX = 200*10**4
    rows = len(triangle)
    dp = []
    for i in range(rows):
        dp.append([])
        for j in range(0,i+1):
            dp[i].append(-1)
    for m in range(rows):
        for n in range(0,m+1):
            # print(m,n)
            if m == 0 and n == 0:
                dp[0][0] = triangle[0][0]
                continue
            up = INT_MAX
            diag = INT_MAX
            if m > 0 and m != n:
                up = dp[m-1][n]
            if m > 0 and n > 0:
                diag = dp[m-1][n-1]
            ans = triangle[m][n] + min(up,diag)
            dp[m][n] = ans
            # print(m,n,ans)
    return min(dp[-1])

tri1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
tri2 = [[-10]]
print("tri1",minimumTotal(tri1))
print("tri2",minimumTotal(tri2))