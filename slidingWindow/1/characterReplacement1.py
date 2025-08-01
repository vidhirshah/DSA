def characterReplacement(s,k):
    maxlen = 0
    length = len(s)
    left = 0
    freq = [0]*26
    for right in range(length):
        freq[ord(s[right])-ord('A')] += 1
        subarrray_length = right-left + 1
        if subarrray_length - max(freq) <= k:
            maxlen = max(maxlen,right-left+1)
        else:
            freq[ord(s[left])-ord('A')] -= 1
            left += 1
    return maxlen

s = "AABABBA"
k = 3
print(characterReplacement(s,k))