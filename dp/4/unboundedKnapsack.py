def unboundedKnapsack(wt:list, val:list, n, W):
    def helper(n,weight):
        if n == 0:
            return 0
        print(n,weight,wt[n-1],W)
        if weight >= W:
            return 0
        nottaken = helper(n-1,weight)
        taken = 0
        if weight + wt[n-1] <= W:
            taken = val[n-1] + helper(n,weight + wt[n-1])
        return max(taken ,nottaken)
    return helper(len(val),0)

val = [10, 40, 50, 70]
wt = [1,3,4,5]
W = 8
print(unboundedKnapsack(wt,val,len(val),W))