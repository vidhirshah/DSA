def solveNQueens(n):
    result = []
    ans = []
    def isSafe(row,col):
        cols = []
        for r in range(len(ans)):
             c = ans[r].index('Q')
             if col == c:
                  return False
             if abs(r-row) == abs(col -c):
                  return False
        return True
    
    def helper(i):
        if i >= n:
            return result.append(ans[:])
        for col in range(n):
                if isSafe(i,col):
                    ans.append("."*col+"Q"+"."*(n-1-col))
                    helper(i+1)
                    ans.pop()   
        return
    helper(0)
    return result

n = 1
print(solveNQueens(n))