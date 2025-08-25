def trap(height: list[int]) -> int:
    n = len(height)
    if n== 0 or n == 1:
        return 0
    left = height[0]
    suffix = [0]*n
    right = 0
    for i in range(n-1,-1,-1):
        suffix[i] = right
        right = max(right,height[i])
    total = 0
    for i in range(1,n):
        right = suffix[i]
        if height[i] <= left and height[i] <= right:
            level = min(left,right)
            total += (level - height[i])
        left = max(left,height[i])
    return total


height = [0,7,1,4,6]
print(height)
print(trap(height))