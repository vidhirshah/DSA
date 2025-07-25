def isAnagram(s,t):
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    freq = [0]*26
    for i in s:
        freq[ord(i)-ord('a')] += 1
    for i in t:
        freq[ord(i)-ord('a')] -= 1
    for i in freq:
        if i != 0:
            return False
    return True

s = "a"
t = "nagaram"
print(isAnagram(s,t))