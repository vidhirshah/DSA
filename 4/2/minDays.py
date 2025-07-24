def ifPossible(bloomDay,m,k,d):
    count = 0
    for i in bloomDay:
        if i <= d:
            count = count + 1
            if count == k:
                m = m - 1
                count = 0
        else:
            count = 0
    if m <= 0:
        return True
    return False

def minDays(bloomDay, m, k):
    if m*k > len(bloomDay):
        return -1
    left = min(bloomDay)
    right = max(bloomDay)
    while left <= right:
        mid = int((left+right)/2)
        if ifPossible(bloomDay,m,k,mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

bloomDay = [1000000000,1000000000]
m = 1 #no of booquets
k = 1 #no of flowers
print(minDays(bloomDay,m,k))    