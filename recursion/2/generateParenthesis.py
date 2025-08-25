def helper(op,cp,n,s):
    if op == cp and op + cp == 2*n:
        return [s]
    res = []
    print(op,cp,n)
    if op < n:
        res.extend(helper(op+1,cp,n,"("))
    if op > cp:
        res.extend(helper(op,cp+1,n,")"))
    for i in range(len(res)):
        res[i] = s + res[i]
    return res

def generateParenthesis(n):
    return helper(0,0,n,"")

n = 1
print(generateParenthesis(n))