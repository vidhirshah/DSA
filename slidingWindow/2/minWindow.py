def minWindow(s,t):
    m = len(s)
    n = len(t)
    if m < n:
        return ""
    minimum = m
    output = ""
    hash = {}
    for i in t:
        hash[i] = 1 + hash.get(i,0)
    for i in range(m):
        hash = {}
        for j in t:
            hash[j] = 1 + hash.get(j,0)
        count = 0
        for j in range(i,m):
            if hash.get(s[j],0) == 0:
                hash[s[j]] = -1
            else:
                hash[s[j]] -= 1
                if hash[s[j]] >= 0:
                    count += 1
            if count == n:
                if minimum >= j - i + 1:
                    minimum = j - i + 1
                    output = s[i:j+1]
                    break
    return output

s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
print(minWindow(s,t))