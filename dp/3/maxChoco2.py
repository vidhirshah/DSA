def maxChocolates(g):
    dp = []
    length = len(g)
    INT_MIN = -10**4
    for i in range(length):
        dp.append([])
        for j in range(length):
            dp[i].append([])
            for k in range(length):
                dp[i][j].append(-1)
    dp[0][0][length-1] = g[0][0]   + g[0][length-1]
    for m in range(1,length):
        for n1 in range(length):
            for n2 in range(length):
                maxi = INT_MIN
                if m == 1  :
                    for d1 in range(-1,2):
                        for d2 in range(-1,2):
                            if n1 + d1 == 0 and n2 + d2 == length -1:
                                maxi = max(dp[m-1][n1+d1][n2+d2],maxi)
                if m > 1:
                    for d1 in range(-1,2):
                        for d2 in range(-1,2):
                            if n1 + d1 >= 0 and n1 + d1 <= length -1 and n2 + d2 >= 0 and n2 + d2 <= length -1:
                                maxi = max(dp[m-1][n1+d1][n2+d2],maxi)
                if n1 == n2:
                    ans =  maxi + g[m][n1]
                else:
                    ans =  maxi + g[m][n1]+g[m][n2]
                dp[m][n1][n2] = ans
    return max(dp[length-1][c1][c2] for c1 in range(length) for c2 in range(length) if dp[length-1][c1][c2] != -1)

i1 =  [[2, 3, 1, 2],[3, 4, 2, 2],[5, 6, 3, 5]]
i2 = [[1, 2],[3, 4]]
print("i1",maxChocolates(i1))
print("i2",maxChocolates(i2))