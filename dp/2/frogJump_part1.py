def frogJump(heights):
    if len(heights) == 0 or len(heights) == 1:
        return 0
    if len(heights) == 2:
        return frogJump(heights[1:])+abs(heights[0]-heights[1])
    return min(frogJump(heights[1:])+abs(heights[0]-heights[1]),frogJump(heights[2:])+abs(heights[0]-heights[2]))

heights = [7, 5, 1, 2, 6]
print(frogJump(heights))