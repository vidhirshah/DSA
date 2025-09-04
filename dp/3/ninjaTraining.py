def ninjaTraining(matrix):
    def helper(day,task):
        if day > len(matrix) -1 :
            return 0
        print(day,task)
        maxi = 0
        for i in range(3):
            if i != task:
                maxi = max(maxi,helper(day+1,i)+matrix[day][i])
        return maxi 
    return helper(0,3)

matrix =   [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
# matrix = [[10, 40, 70], [20, 50, 80], [30,  60, 90]]
print(ninjaTraining(matrix))