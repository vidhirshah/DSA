def minimumTotal(triangle: list[list[int]]):
    dp = []
    for i in range(len(triangle)):
        dp.append([])
        for j in range(0,i+1):
            dp[i].append(-1)
    print(dp)
    def helper(m,n):
        INT_MAX = 200*10**4
        rows = len(triangle)
        # if n > m :
        #     return INT_MAX
        if m >= rows:
            return INT_MAX
        print(m,n)
        down = INT_MAX
        diag = INT_MAX
        if m == rows - 1:
            return triangle[m][n]
        if m < rows - 1:
            down = helper(m+1,n)
        if m < rows -1 and n < rows - 1:
            diag = helper(m+1,n+1)
        ans = triangle[m][n] + min(down,diag)
        # print(m,n,ans)
        return ans
    return helper(0,0)

tri1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
tri2 = [[-10]]
print("tri1",minimumTotal(tri1))
print("tri2",minimumTotal(tri2))