def candy(ratings):
    length = len(ratings)
    i = 1
    sum = 1
    peak = 1
    while i < length:
        if ratings[i-1] == ratings[i]:
            sum += 1
            i += 1
            continue
        peak = 1
        while i < length and ratings[i] > ratings[i-1]:
            peak += 1
            sum += peak
            i += 1
        down = 1
        while i < length and ratings[i] < ratings[i-1]:
            down += 1
            sum += down
            print(i,peak,down,sum)
            i += 1
        if peak < down:
            sum += down - peak

    return sum

ratings = [1,0,5]
print(candy(ratings))