def addOperators(nums,target):
    result = []
    def helper(index,total,sol):
        if index == len(num):
            if total == target:
                result.append(sol)
            return 
        no = ord(nums[index]) - ord('0')
        print(no,sol)
        sol = sol + "*" + nums[index]
        helper(index+1,total*no,sol)
        sol = sol[:-2]
        sol = sol + "+" + nums[index]
        helper(index+1,total+no,sol)
        sol = sol[:-2]
        sol = sol + "-" + nums[index]
        helper(index+1,total-no,sol)
        sol = sol[:-2]
        return
    helper(1,ord(nums[0]) - ord('0'),nums[0])
    return result

num = '232'
target = 8
print(addOperators(num,target))