def findMissingRepeatingNumbers(nums):
    n = len(nums)
    sum_n = int(n *(n+1)/2)
    sum = 0
    sum_sq = 0
    sum_sq_n = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        sum_sq = sum_sq + nums[i]**2
        sum_sq_n = sum_sq_n + (i+1)**2
    squares = sum_sq_n - sum_sq
    diff = sum_n - sum
    sum = int(squares/diff)
    x = int((sum + diff)/2)
    y = sum - x
    return [y,x]

print(findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))