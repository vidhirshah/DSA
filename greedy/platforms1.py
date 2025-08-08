def findPlatform(arrival,departure):
    platforms = 0
    arr = []
    for i in arrival:
        arr.append([i,'a'])
    for i in departure:
        arr.append([i,'d'])
    arr.sort(key=lambda x:x[0])
    count = 0
    for i in arr:
        if i[1] == 'a':
            count += 1
        else:
            count -= 1
        platforms = max(platforms,count)
    return platforms

arrival = [900, 940, 950, 1100, 1500, 1800] 
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(findPlatform(arrival,departure))