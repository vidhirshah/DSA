def longestCommonPrefix(strs):
    prefix = ""
    pref_len = len(strs[0])
    for i in strs:
        pref_len = min(len(i),pref_len)
    for i in range(pref_len):
        flag = 1
        for j in range(len(strs)-1):
            if strs[j][i] != strs[j+1][i]:
                flag = 0
        if flag == 1:
            prefix = prefix + strs[0][i]
            print(prefix)
        else:
            break
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))