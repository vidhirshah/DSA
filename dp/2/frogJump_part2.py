INT_MAX = 2**31-1
def helper(heights,k,n):
    if n <= 0:
        return 0
    ans = INT_MAX
    for i in range(1,k+1):
        if n-i >= 0:
            ans = min(ans,helper(heights,k,n-i)+abs(heights[n]-heights[n-i]))
    return ans

def frogJump(heights,k):
    return helper(heights,k,1)

heights = [7, 5, 1, 2, 6]
k = 2
print(frogJump(heights,k))