def unboundedKnapsack(val:list,N):
    def helper(n,cuts):
        if n >= N:
            return 0
        if cuts >= N:
            return 0
        nottaken = helper(n+1,cuts)
        taken = 0
        if cuts + n +1 <= N:
            taken = val[n] + helper(n,cuts + n+1)
        return max(taken ,nottaken)
    return helper(0,0)

val = [1, 6, 8, 9, 10, 19, 7, 20]
N = 8
val = [1, 5, 8, 9]
N = 4
print(unboundedKnapsack(val,N))