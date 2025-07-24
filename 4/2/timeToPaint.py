def requiredPainters(B,C,time):
    painters = 1
    boards = 0
    for i in C:
        if boards + i <= time:
            boards += i
        else:
            painters +=1
            boards = i
    return painters

def paint(A,B,C):
    left = max(C)
    right = sum(C)
    while left <= right:
        mid = int((left+right)/2)
        if requiredPainters(B,C,mid) > A:
            left = mid + 1
        else:
            right = mid -1
    return (left*B)%10000003

A = 1
B = 1000000
C = [1,1,1,1]
print(paint(A,B,C))