def fractionalKnapsack(val, wt, cap):
    arr = []
    for i in range(len(val)):
        arr.append([val[i],wt[i]])
    arr.sort(key = lambda x:x[0]/x[1],reverse=True)
    bag = 0
    profit = 0
    i = 0
    while bag < cap and i < len(val):
        if bag + arr[i][1] <= cap:
            bag += arr[i][1]
            profit += arr[i][0]
        else:
            req = capacity - bag
            req = req/arr[i][1]
            profit += req*arr[i][0]
        i += 1

    # for i in arr:
    #     if bag + i[1] <= capacity:
    #         bag += i[1]
    #         profit += i[0]
    #     else:
    #         req = capacity - bag
    #         req = req/i[1]
    #         profit += req*i[0]
    return profit

val =  [60,100,120]
wt = [10,20,30]
capacity = 50
print(fractionalKnapsack(val,wt,capacity))