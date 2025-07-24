def possible(weights,days,min_wight):
    weights_sum = 0
    for i in weights:
        weights_sum = weights_sum + i
        if weights_sum == min_wight:
            days = days - 1
            weights_sum = 0
        elif weights_sum > min_wight:
            days = days - 1
            weights_sum = i
    if weights_sum and weights_sum <= min_wight:
        days = days - 1
    if days >= 0 :
        return True
    return False

def shipWithinDays(weights, days):
    left = max(weights)
    if days == len(weights):
        return left
    right = sum(weights)
    if days == 1:
        return right
    while left <= right:
        mid = int((left+right)/2)
        print(left,mid,right,possible(weights,days,mid))
        if possible(weights,days,mid):
            right = mid - 1
        else: 
            left = mid + 1
    return left

weights = [3,3,3,3,3,3]
days = 2
print(shipWithinDays(weights,days))
