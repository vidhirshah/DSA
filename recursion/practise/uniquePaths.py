def uniquePaths(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 1:
        ans = uniquePaths(m,n-1)
    elif n == 1:
        ans = uniquePaths(m-1,n)
    else:
        ans = uniquePaths(m,n-1) + uniquePaths(m-1,n)
    return ans

print(uniquePaths(3,2))