def kDistinctChar(s,k):
    total = 0
    maxTotal = 0
    left = 0
    hash = {}
    for right in range(len(s)-1):
        hash[s[right]] = 1 + hash.get(s[right],0)
        if len(hash) > k:
            while len(hash) > k:
                hash[s[left]] = hash[s[left]] -1
                if hash[s[left]] == 0:
                    hash.pop(s[left])
                left += 1
        if len(hash) <= k:
            maxTotal = max(maxTotal,right-left+1)
    return maxTotal

s = "aababbcaacc"
k = 2
s = "abcddefg"
k = 3
print(kDistinctChar(s,k))