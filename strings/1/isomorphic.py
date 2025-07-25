def isIsomorphic(s,t):
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    s_to_t = {}
    t_to_s = {}
    for i in range(s_len):
        if s[i] in s_to_t.keys():
            if s_to_t[s[i]] != t[i]:
                return False
        else:
            s_to_t[s[i]] = t[i]
        if t[i] in t_to_s.keys():
            if t_to_s[t[i]] != s[i]:
                return False
        else:
            t_to_s[t[i]] = s[i]
    return True

# s = "paper"
# t = "title"
s = "badc"
t = "baba"
print(isIsomorphic(s,t))