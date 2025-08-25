def helper(n,i):
    if n < 1:
        return []
    if n == 0:
        if i == "1":
            return ["1"]
        else:
            return ["0"]
    part1 = helper(n-1,"0")
    if i == "1":
        part2 = []
    else:
        part2 = helper(n-1,"1")
    result = part1 + part2
    for j in range(len(result)):
        result[j] = i + result[j]
    return result

def generateBinaryStrings(n):
    return helper(n,"0") + helper(n,"1")

n = 3
print(generateBinaryStrings(n))