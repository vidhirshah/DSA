def numberOfSubstrings(s):
    count = 0
    length = len(s)
    for i in range(length-2):
        hash = set()
        for j in range(i,length):
            if s[j] not in hash:
                hash.add(s[j])
            if len(hash) == 3:
                count += length - j
                break
    return count

s = "abcabc"
print(numberOfSubstrings(s))