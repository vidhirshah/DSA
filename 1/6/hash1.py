def hash(arr):
    arr_max = max(arr)
    temp_hash = [0]*(arr_max + 1)
    for i in arr:
        temp_hash[i] = temp_hash[i] + 1
    return temp_hash

print(hash([4,2,8,3,5,6,4,3,8,6,0,5,3,6,7,8,9,3,2,3,5,6,7,8,3,4,2,6,4,7,8,5,3,5,7,3]))