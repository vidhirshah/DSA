def check(nums): 
    pointer = -1
    for i in range(1,len(nums)):
        if nums[i - 1] > nums[i]:
            pointer = i
            break
    if pointer == -1:
        return True
    elif nums[-1] > nums[0]:
        return False 
    for i in range(pointer+1,len(nums)):
        if nums[i - 1] > nums[i] :
            return False
    return True
arr = [3,4,6,8,1,5,2]
print(check(arr))