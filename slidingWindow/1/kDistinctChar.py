def kDistinctChar(s,k):
    total = 0
    maxTotal = 0
    hash = set()
    for i in range(len(s)-1):
        hash = set()
        total = 0
        for j in range(i,len(s)):
            hash.add(s[j])
            if len(hash) <= k:
                total += 1
            else:
                maxTotal = max(maxTotal,total)
                break
    return maxTotal

# s = "aababbcaacc"
# k = 2
s = "abcddefg"
k = 3
print(kDistinctChar(s,k))