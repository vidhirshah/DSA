def eraseOverlapIntervals(intervals):
    intervals.sort(key= lambda x:x[1])
    end = intervals[0][1]
    ans = 0
    for i in intervals[1:]:
        if i[0] < end:
            ans += 1
        else:
            end = i[1]
    return ans

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
