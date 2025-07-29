def totalFruits(fruits):
    total = 0
    maxTotal = 0
    left = 0
    hash = {}
    for right in range(len(fruits)-1):
        hash[fruits[right]] = 1 + hash.get(fruits[right],0)
        print(hash,fruits[left])
        if len(hash) > 2:
            while len(hash) > 2:
                hash[fruits[left]] = hash[fruits[left]] -1
                if hash[fruits[left]] == 0:
                    hash.pop(fruits[left])
                left += 1
        if len(hash) <= 2:
            maxTotal = max(maxTotal,right-left+1)
    return maxTotal

fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruits(fruits))