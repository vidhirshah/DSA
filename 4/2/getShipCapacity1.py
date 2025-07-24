def possible(weights,days,min_wight):
    capacity = 0
    d = 1
    for i in weights:
        if capacity + i > min_wight:
            d += 1
            capacity = 0
        capacity += i
    return d <= days

def shipWithinDays(weights, days):
    left = max(weights)
    if days == len(weights):
        return left
    right = sum(weights)
    if days == 1:
        return right
    while left <= right:
        mid = int((left+right)/2)
        if possible(weights,days,mid):
            right = mid - 1
        else: 
            left = mid + 1
    return left

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights,days))
