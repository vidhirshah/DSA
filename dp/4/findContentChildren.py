def findContentChildren(g:list,s:list):
    g.sort()
    s.sort()
    i = 0
    j = 0
    length_g = len(g)
    length_s = len(s)
    i = 0
    j = 0
    count = 0
    while i < length_g and j < length_s:
        # print(i,j)
        
        if g[i] <= s[j] :
            count += 1
            i += 1
            j += 1
        while j < length_s and i < length_g  and  g[i] > s[j]:
            j += 1   
    return count

g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))