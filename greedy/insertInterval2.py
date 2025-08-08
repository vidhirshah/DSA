def insert(intervals,newInterval):
    result = []
    length = len(intervals)
    if length == 0:
        return [newInterval]
    i = 0
    while i < length and newInterval[0] > intervals[i][1]:
        result.append(intervals[i])
        i += 1
    while i < length and newInterval[1] >= intervals[i][0]:
        newInterval[0] = min(newInterval[0],intervals[i][0])
        newInterval[1] = max(newInterval[1],intervals[i][1])
        i += 1
    result.append(newInterval)
    while i < length:
        result.append(intervals[i])
        i += 1
    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals,newInterval))
