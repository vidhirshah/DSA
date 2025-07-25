def rotateString(s , goal):
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        is_same = 1
        rotated = s[i+1:]+s[:i+1]
        for j in range(len(s)):
            if rotated[j] != goal[j]:
                is_same = 0
                break
        if is_same == 1:
            return True
    return False

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))