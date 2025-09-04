def ninjaTraining(matrix):
    dp = [-1,-1,-1,-1]
    dp[0] = max(matrix[0][1],matrix[0][2])
    dp[1] = max(matrix[0][0],matrix[0][2])
    dp[2] = max(matrix[0][1],matrix[0][0])
    dp[3] = max(matrix[0][1],matrix[0][2],matrix[0][0])
    for i in range(1,len(matrix)):
        dp[3] = 0
        dp1 = [-1]*4
        for last in range(4):
            maxi = 0
            for task in range(3):
                if task != last:
                    maxi = max(maxi,dp[task]+ matrix[i][task])
            dp1[last] = maxi
        dp = dp1
        #    print(dp)
    return dp[3]

# matrix =   [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
matrix = [[10, 40, 70], [20, 50, 80], [30,  60, 90]]
print(ninjaTraining(matrix))