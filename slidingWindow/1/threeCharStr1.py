def numberOfSubstrings(s):
    count = 0
    length = len(s)
    left = 0
    hash = {}
    for right in range(length):
        hash[s[right]] = 1 + hash.get(s[right],0)
        if len(hash) == 3:
            while len(hash) == 3:
                count += length - right
                if hash[s[left]] == 1:
                    hash.pop(s[left])
                else:
                    hash[s[left]] -= 1
                left += 1
    return count

s = "bbacba"
print(numberOfSubstrings(s))