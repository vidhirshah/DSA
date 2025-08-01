def numberOfSubstrings(s):
    count = 0
    length = len(s)
    left = 0
    hash = [-1]*3
    for right in range(length):
        hash[ord(s[right])-ord('a')] = right
        index = min(hash)
        if min != -1:
            count +=( index + 1)
    return count

s = "aaabc"
print(numberOfSubstrings(s))