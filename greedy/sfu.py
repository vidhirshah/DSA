def solve(bt):
    bt.sort()
    sum = 0
    total_time = 0
    for i in range(0,len(bt)-1):
        sum +=bt[i]
        total_time += sum
        print(bt[i],sum,total_time)
    return round(total_time/len(bt))

bt = [4,3,7,1,2]
print(solve(bt))