def findContentChildren(g,s):
    g.sort()
    s.sort()
    count = 0
    child = 0
    cookie = 0
    print(g,s)
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            count += 1
            cookie += 1
            child += 1
        else:
            while child < len(g) and cookie < len(s) and s[cookie] < g[child]:
                cookie += 1
    return count

g = [1,2,3]
s = [1,1]
print(findContentChildren(g,s))