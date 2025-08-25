def trap(height: list[int]) -> int:
    n = len(height)
    if n== 0 or n == 1:
        return 0
    left = height[0]
    right = max(height[1:])
    total = 0
    for i in range(1,n):
        if height[i] >= left or height[i] >= right:
            pass
        else:
            level = min(left,right)
            total += (level - height[i])
        if i < n-1 and height[i] == right:
            right = max(height[i+1:])
        left = max(left,height[i])
    return total
height = [0,7,1,4,6]
print(height)
print(trap(height))