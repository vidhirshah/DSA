def frogJump(heights,k):
    n = len(heights)
    storage = [0]*k
    ans = 0
    INT_MAX = 2**31-1
    for i in range(n):
        ans = INT_MAX
        print(i,storage)
        p = 0
        for j in range(1,k+1):
            if i-j >= 0:
                ans = min(ans,storage[j-1]+abs(heights[i]-heights[i-j]))
                print(i,j,i-j,ans)
        for j in range(1,p):
            storage[j-1] = storage[j]
        if ans == INT_MAX:
            storage[-1] = 0
        else:
            storage[-1] = ans
    return storage[-1]

heights =   [10, 5, 20, 0, 15]
k = 2
print(frogJump(heights,k))