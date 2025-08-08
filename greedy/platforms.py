def findPlatform(arrival,departure):
    platforms = 0
    added = [0]*len(arrival)
    while 0 in added:
        print(added)
        start = added.index(0)
        end = departure[start]
        added[start] = 1
        for i in range(start+1,len(arrival)):
            if end < arrival[i]:
                added[i] = 1
                end = departure[i]
        platforms += 1
    return platforms

arrival = [900, 940, 950, 1100, 1500, 1800] 
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(findPlatform(arrival,departure))