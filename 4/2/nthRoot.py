def nthRoot(n,m):
    left = 1
    right = int(m)
    while left<=right:
        mid = int((left+right)/2)
        power = pow(mid,n)
        if power == m:
            return mid
        elif power < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for i in (1,6,8,27,60,64,100):
    print(i,nthRoot(3,i))
