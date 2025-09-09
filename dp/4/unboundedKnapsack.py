def unboundedKnapsack(wt:list, val:list, n, W):
    def helper(n,weight):
        if n == 0:
            return 0
        print(n,weight,wt[n-1],W)
        # if weight >= W:
        #     return 0
        nottaken = helper(n-1,weight)
        taken = 0
        if weight + wt[n-1] <= W:
            taken = val[n-1] + helper(n,weight + wt[n-1])
        return taken + nottaken
    return helper(len(val),0)

val = [5, 11, 13]
wt = [2, 4, 6]
W = 10
print(unboundedKnapsack(wt,val,len(val),W))