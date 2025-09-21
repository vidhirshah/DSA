def longestCommonSubsequence( word1: str, word2: str):
    def helper(p1,p2):
        if p2 < 0:
            return 1 + p1
        if p1 < 0:
            return 1 + p2
        if word1[p1] == word2[p2]:
            return helper(p1-1,p2-1) 
        else:
            return 1 + min(helper(p1-1,p2-1),helper(p1,p2-1),helper(p1-1,p2))
    return helper(len(word1)-1,len(word2)-1)

s1 = "intention"
s2 = "execution"
print(longestCommonSubsequence(s1,s2))