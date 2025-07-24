def findMissingRepeatingNumbers(nums):
    a = 0
    b = 0
    hash = [0]*len(nums)
    for i in nums:
        hash[i-1] = hash[i-1] + 1
    for i in range(len(hash)):
        if hash[i] == 2:
            a = i + 1
        if hash[i] == 0:
            b = i + 1
    return[a,b]

print(findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))