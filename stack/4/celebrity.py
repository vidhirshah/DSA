def celebrity(m):
    top = 0
    down = len(m) - 1
    while top < down:
        if m[top][down] == 1:
            top += 1
        elif m[down][top] == 1:
            down -= 1
        elif top != down:
            top += 1
            down -= 1
    if top > down:
        return -1
    for i in range(len(m)):
        if m[top][i] == 1:
            return -1
    for i in range(len(m)):
        if i == down and m[i][down] == 1:
            return -1
        if i != down and m[i][down] == 0:
            return -1
    return top

m = [ [0,1] ,[1,0]]
print(celebrity(m))