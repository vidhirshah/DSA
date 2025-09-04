def ninjaTraining(matrix):
    dp = []
    for i in range(len(matrix)):
        dp.append([])
        for j in range(4):
            dp[i].append(-1)
    def helper(day,task):
        if dp[day][task] != -1:
            return dp[day][task]
        print(day,task)
        if day == len(matrix) -1 :
            maxi = 0
            for i in range(3):
                if i != task:
                    maxi = max(maxi,matrix[day][i])
            dp[day][task] = maxi
            return maxi
        maxi = 0
        for i in range(3):
            if i != task:
                maxi = max(maxi,helper(day+1,i)+matrix[day][i])
        dp[day][task] = maxi
        return maxi 
    return helper(0,3)

# matrix =   [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
matrix = [[10, 40, 70], [20, 50, 80], [30,  60, 90]]
print(ninjaTraining(matrix))