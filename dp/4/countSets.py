def isSubsetSum(arr,target):
    def helper(index,sum,count):
        if sum == 0:
            return count + 1
        if index >= len(arr):
            return 0
        return helper(index+1,sum-arr[index],count) + helper(index+1,sum,count)
    return helper(0,target,0)

arr =  [1, 2, 3, 4,5
        ]
t = 5
print(isSubsetSum(arr,t))