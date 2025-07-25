def isAnagram(s,t):
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    s = sorted(s)
    t = sorted(t)
    for i in range(s_len):
        if s[i] != t[i]:
            return False
    return True

s = "s"
t = "nagaram"
print(isAnagram(s,t))