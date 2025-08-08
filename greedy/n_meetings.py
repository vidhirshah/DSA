def maxMeetings(start,end):
    arr = []
    for i in range(len(start)):
        arr.append([start[i],end[i]])
    return arr

start = [1, 3, 0, 5, 8, 5] 
end = [2, 4, 6, 7, 9, 9]
print(maxMeetings(start,end))