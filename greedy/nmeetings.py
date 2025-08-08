def maxMeetings(start,end):
    arr = []
    for i in range(len(start)):
        arr.append([start[i],end[i]])
    arr.sort(key =lambda x: x[1])
    sol = []
    meet_end = 0
    for i in arr:
        if meet_end >= i[0]:
            continue
        else:
            sol.append(i)
            meet_end = i[1]
    return len(sol)

start = [1, 3, 0, 5, 8, 5] 
end = [2, 4, 6, 7, 9, 9]
print(maxMeetings(start,end))