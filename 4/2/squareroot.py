def floorSqrt(n):
    left = 0
    right = int(n/2)
    ans = 1
    while left <= right:
        mid = int((left+right)/2)
        sqrt = mid*mid
        if sqrt > n:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return right

for i in [20,28,36,100,120,160]:
    print(i,floorSqrt(i))