def minimiseMaxDistance(arr,k):
    n = len(arr)
    distance = [0]*(n-1)
    gas_stations = 0
    for stations in range(k):
        max_dis = -1
        max_ind = 0
        for i in range(n-1):
            mid_dis = (arr[i+1] - arr[i])/(distance[i] + 1)
            if mid_dis > max_dis:
                max_dis = mid_dis
                max_ind = i
        distance[max_ind] += 1
    max_dis = -1
    for i in range(n-1):
        mid_dis = (arr[i+1] - arr[i])/(distance[i] + 1)
        max_dis = max(max_dis,mid_dis)
    return max_dis

arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 1
print(minimiseMaxDistance(arr,k))