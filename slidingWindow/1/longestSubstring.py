def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    maxLen = 0
    ferq = {}
    while right < len(s):
        if s[right] not in ferq.keys():
            ferq[s[right]] = right
            right += 1
        else:
            maxLen = max(maxLen,right-left)
            if ferq[s[right]] + 1 >= left:
                left = ferq[s[right]] + 1
            ferq.pop(s[right])
        print(ferq)
        print(left,right,maxLen)
    maxLen = max(maxLen,right-left)
    return maxLen

s = "tmmzuxt"
print(s)
print(lengthOfLongestSubstring(s))