def candy(ratings):
    left = [1]*len(ratings)
    right = [1]*len(ratings)
    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            left[i] = (left[i-1]+1)
    for i in range(len(ratings)-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i+1]+1
    sum = 0
    for i in range(0,len(ratings)):
        sum += max(left[i],right[i])                
    return sum

ratings = [1,0,5]
print(candy(ratings))