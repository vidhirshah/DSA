def ninjaTraining(matrix):
    def helper(day,task):
        if day > len(matrix) -1 :
            return 0
        if task == 0:
            return matrix[day][task] + max(helper(day+1,1),helper(day+1,2))
        elif day == 1:
            return matrix[day][task] + max(helper(day+1,0),helper(day+1,2))
        else:
            return matrix[day][task] + max(helper(day+1,0),helper(day+1,1))
        return
    return max(helper(0,0),helper(0,1),helper(0,2))

matrix =   [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
print(ninjaTraining(matrix))