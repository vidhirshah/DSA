def maxScore(cardPoints,k):
    maxSum = 0
    length = len(cardPoints)
    left = k-1
    right = length -1
    sum = 0
    for i in range(k):
        sum += cardPoints[i]
    maxSum = sum
    for i in range(k):
        sum -= cardPoints[left]
        left -= 1
        sum += cardPoints[right]
        right -= 1
        maxSum = max(sum,maxSum)
    return maxSum

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxScore(cardPoints,k))