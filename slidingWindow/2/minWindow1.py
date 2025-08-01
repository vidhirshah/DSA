def minWindow(s,t):
    m = len(s)
    n = len(t)
    if m < n:
        return ""
    minimum = m
    output = ""
    left = 0
    count = 0
    right = 0
    hash = {}
    for i in t:
        hash[i] = 1 + hash.get(i,0)
    while right < m:
        print(hash)
        if hash.get(s[right],0) == 0:
            hash[s[right]] = -1
        else:
            hash[s[right]] -= 1
            if hash[s[right]] >= 0:
                count += 1
        print(left,right,count)
        while count == n:
            if minimum >= right - left + 1:
                minimum = right - left + 1
                output = s[left:right+1]
            hash[s[left]] += 1
            if hash[s[left]] > 0:
                count -= 1
            left += 1
        right += 1
    return output

s = "ADOBECODEBANC"
t = "ABC"
print(s)
print(minWindow(s,t))