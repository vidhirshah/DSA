def maxChocolates(g):
    def helper(m,n1,n2):
        length = len(g)
        INT_MIN = -10**4
        if m >= length or n1 >= length or n2 >= length:
            return INT_MIN
        if n1 < 0 or n2 < 0:
            return INT_MIN
        if m == length - 1:
            if n1 == n2:
                return g[m][n1]
            return g[m][n1] + g[m][n2]
        maxi = INT_MIN
        for d1 in range(-1,2):
            for d2 in range(-1,2):
                maxi = max(helper(m+1,n1+d1,n2+d2),maxi)
        print(m,n1,n2,maxi)
        if n1 == n2:
            return maxi + g[m][n1]
        return maxi + g[m][n1]+g[m][n2]
    return helper(0,0,len(g)-1)

i1 =  [[2, 3, 1, 2],[3, 4, 2, 2],[5, 6, 3, 5]]
i2 = [[1, 2],[3, 4]]
print("i1",maxChocolates(i1))
print("i2",maxChocolates(i2))