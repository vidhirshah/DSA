def hackerlandRadioTransmitters(x:list, k):
    i = 0
    n = len(x)
    radars = 0
    x = sorted(x)
    print(x)
    while i < n:
        point = x[i] + k
        while i < n and x[i] <= point:
            i += 1
        radars += 1
        point_next = x[i-1] + k
        while i < n and x[i] <= point_next:
            i += 1
    return radars

x = [7, 2, 4 ,6 ,5 ,9 ,12, 11 ]
k = 2
print(hackerlandRadioTransmitters(x,k))