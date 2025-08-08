def candy(ratings):
    length = len(ratings)
    left = [1]*length
    for i in range(1,length):
        if ratings[i] > ratings[i-1]:
            left[i] = (left[i-1]+1)
    sum = max(left[length-1],1)
    for i in range(length-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            left[i] = max(left[i],left[i+1]+1)
        sum += left[i]
    return sum

ratings = [1,0,5]
print(candy(ratings))