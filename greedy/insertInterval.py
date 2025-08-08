def insert(intervals,newInterval):
    result = []
    length = len(intervals)
    if length == 0:
        return [newInterval]
    if intervals[-1][0] <= newInterval[0]:
        intervals.insert(length,newInterval)
    else:
        for i in range(length):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i,newInterval)
    start = intervals[0][0]
    end = intervals[0][1]
    for i in intervals[1:]:
        if i[0] <= end:
            end = max(end,i[1])
        else:
            result.append([start,end])
            start = i[0]
            end = i[1]
    if len(result) == 0 or result[-1][1] != end:
        result.append([start,end])
    return result

    # while t < len(intervals):
    #     if len(result) > 0:
    #         if result[-1][0] < newInterval[0] and newInterval[0] <= start :
    #             start = newInterval[0]
    #             end = max(end,newInterval[1])
    #     if start <= newInterval[0] and newInterval[0] <= end:
    #         end = max(end,newInterval[1])
    #     i = intervals[t]
    #     print("s",t,i,start,end)
    #     if i[0] <= end and i[0] >= start:
    #         end = max(end,i[1])
    #         print("a",i,start,end)
    #     else:
    #         result.append([start,end])
    #         start = intervals[t][0]
    #         end = intervals[t][1]
    #     print("e",i,start,end,result)
    #     t += 1
    # if len(result) == 0 or end != result[-1][1]:
    #     result.append([start,end])
    # return result

intervals = [[1,3],[9,10]]
newInterval = [4,8]
print(insert(intervals,newInterval))
