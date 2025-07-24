def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    result = []
    for i in intervals[1:]:
        if i[0] <= end:
            if i[1] > end:
                end = i[1]
        else:
            result.append([start,end])
            start = i[0]
            end = i[1]
    if len(result) == 0 or end != result[-1][1]:
        result.append([start,end])
    return result

intervals = [[1,4],[2,3]]
print(merge(intervals))