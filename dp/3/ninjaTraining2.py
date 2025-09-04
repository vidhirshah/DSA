def ninjaTraining(matrix):
    dp = []
    for i in range(len(matrix)):
        dp.append([])
        for j in range(4):
            dp[i].append(-1)
    dp[0][0] = max(matrix[0][1],matrix[0][2])
    dp[0][1] = max(matrix[0][0],matrix[0][2])
    dp[0][2] = max(matrix[0][1],matrix[0][0])
    dp[0][3] = max(matrix[0][1],matrix[0][2],matrix[0][0])
    for i in range(1,len(matrix)):
        dp[i][3] = 0
        for last in range(4):
            maxi = 0
            for task in range(3):
                if task != last:
                    maxi = max(maxi,dp[i-1][task]+ matrix[i][task])
            dp[i][last] = maxi
        print(dp)
    return dp[len(matrix)-1][3]

matrix =   [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
# matrix = [[10, 40, 70], [20, 50, 80], [30,  60, 90]]
print(ninjaTraining(matrix))