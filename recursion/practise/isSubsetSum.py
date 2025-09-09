def isSubsetSum(arr,target):
    subset = []
    def helper(index,sum):
        if index >= len(arr):
            if sum == 0:
                return True
            return False
        return helper(index+1,sum-arr[index]) or helper(index+1,sum)
    return helper(0,target)

arr = [1,2,7,3]
t = 19
print(isSubsetSum(arr,t))