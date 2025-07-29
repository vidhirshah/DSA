def totalFruits(fruits):
    total = 0
    maxTotal = 0
    hash = set()
    for i in range(len(fruits)-1):
        hash = set()
        total = 0
        for j in range(i,len(fruits)):
            hash.add(fruits[j])
            if len(hash) <= 2:
                total += 1
            else:
                maxTotal = max(maxTotal,total)
                break
    return maxTotal

fruits = [1, 2, 3, 2, 2]
print(totalFruits(fruits))