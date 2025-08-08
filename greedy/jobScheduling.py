def jobScheduling(jobs):
    jobs.sort(key = lambda x: x[2],reverse = True)
    deadline = jobs[0][1]
    for i in jobs:
        deadline = max(deadline,i[1])
    result = [-1]*(deadline+1)
    profit = 0
    for i in jobs:
        last = i[1]
        while last > 0 :
            if result[last] == -1:
                result[last] = last
                profit += i[2]
                break
            last -= 1
    return profit

jobs =  [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]
print(jobScheduling(jobs))