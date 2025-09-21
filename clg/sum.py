def powerSum(X, N):
    limit = int(pow(X,1/N))
    def helper(number,total):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if number < 1:
            return 0
        nottaken = helper(number-1,total)
        taken = helper(number-1,total - number**n)
        return nottaken + taken
    return helper(limit,X)

x = 100
n = 2
print(powerSum(x,n))