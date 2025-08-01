def characterReplacement(s,k):
    maxlen = 0
    length = len(s)
    for i in range(length-1):
        freq = [0]*26
        for j in range(i,length):
            freq[ord(s[j])-ord('A')] += 1
            max_freq = max(freq)
            subarray_length = j-i + 1
            if subarray_length - max_freq <= k:
                maxlen = max(maxlen,subarray_length)
    return maxlen

s = "ABAB"
k = 2
print(characterReplacement(s,k))