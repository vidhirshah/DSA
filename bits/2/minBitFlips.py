def minBitFlips(start,goal):
    ans = start ^ goal
    count = 0
    while ans > 0:
        count += 1
        ans &= (ans-1)
    return count

start = 10
goal = 7
print(minBitFlips(start,goal))