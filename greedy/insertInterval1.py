def insert(intervals,newInterval):
    result = []
    length = len(intervals)
    if length == 0:
        return [newInterval]
    if newInterval[0] > intervals[-1][1]:
        for i in intervals:
            result.append(i)
        result.append(newInterval)
        return result
    t = 0
    while t < len(intervals):
        i = intervals[t]
        if newInterval[0] <= i[1]:
            if newInterval[0] < i[0] and newInterval[0] <i[1]:
                result.append(newInterval)
                break
            start = min(i[0],newInterval[0])
            end = max(i[1],newInterval[1])
            t+= 1
            for j in range(t,length):
                i = intervals[j]
                if i[0] <= end:
                    end = max(end,i[1])
                else:
                    result.append([start,end])
                    t = j 
                    break
            if len(result) == 0 or result[-1][1] != end:
                result.append([start,end])
            break
        else:
            result.append(i)
            t += 1
    while t < length:
        result.append(intervals[t])
        t += 1
    return result

intervals = [[1,5]]
newInterval = [2,3]
print(insert(intervals,newInterval))
