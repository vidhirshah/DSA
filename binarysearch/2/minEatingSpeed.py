def ifEaten(piles,h,k):
    hours = 0
    for i in piles:
        left = i % k
        hours = int(i/k) + hours
        if left:
            hours = hours + 1
        if hours > h:
            return False
    return True
def minEatingSpeed(piles,h):
    left = 1
    right = max(piles)
    while left<= right:
        mid = int((left+right)/2)
        if ifEaten(piles,h,mid) == True:
            right = mid - 1
        else:
            left = mid + 1
    return left

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles,h))