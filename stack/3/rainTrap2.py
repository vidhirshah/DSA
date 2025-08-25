def trap(height: list[int]) -> int:
    n = len(height)
    if n== 0 or n == 1:
        return 0
    left = 0
    leftmax = height[0]
    right = n-1
    rightmax = height[-1]
    total = 0
    while left != right:
        leftmax = max(leftmax,height[left])
        rightmax = max(rightmax,height[right])
        if height[left] <= leftmax and height[left] <= rightmax:
            level = min(leftmax,rightmax)
            total += (level - height[left])
            left += 1
        elif leftmax >= rightmax:
            if height[right] <= leftmax and height[right] <= rightmax:
                level = min(leftmax,rightmax)
                total += (level - height[right])
                right -= 1
    return total


height = [2,0,2]
print(height)
print(trap(height))