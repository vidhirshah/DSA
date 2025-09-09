def isSubsetSum(arr,target):
    subset = []
    def helper(index,sum):
        if sum == 0:
            return True
        if index >= len(arr):
            return False
        return helper(index+1,sum-arr[index]) or helper(index+1,sum)
    return helper(0,target)

arr = [1,2,7,3]
t = 10
print(isSubsetSum(arr,t))