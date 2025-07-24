def findMedian(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    length = rows*cols
    temp_array = [0]*length
    pointer = 0
    for i in range(rows):
        for j in range(cols):
            temp_array[pointer] = matrix[i][j]
            pointer += 1
    temp_array.sort()
    return temp_array[int(length/2)]

matrix = [ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 
# matrix = [ [1, 3, 8], [2, 3, 4], [1, 2, 5] ]
print(findMedian(matrix))