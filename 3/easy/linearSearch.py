def linearSearch(nums,targert):
    for i in range(len(nums)):
        if nums[i] == targert:
            return i
    return -1

print(linearSearch([2, 3, 4, 5, 3], 6))