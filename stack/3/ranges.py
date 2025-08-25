def sumSubnumsayMins(nums: list[int]) -> int:
    ans = 0
    def pse():
        stack = []
        result = [0]*len(nums)
        for i in range(len(nums)):
            if len(stack) == 0:
                result[i] = -1
            elif nums[i] >= nums[stack[-1]]:
                result[i] = stack[-1]
            else:
                while len(stack) != 0 and nums[i] < nums[stack[-1]]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = -1
                else:
                    result[i] = stack[-1]
            stack.append(i)
        return result
    def nse():
        stack = []
        result = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if len(stack) == 0:
                result[i] = len(nums)
            elif nums[i] > stack[-1][0]:
                result[i] = stack[-1][1]
            else:
                while len(stack) != 0 and nums[i] <= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = len(nums)
                else:
                    result[i] = stack[-1][1]
            stack.append([nums[i],i])
        return result
    def pge():
        stack = []
        result = [0]*len(nums)
        for i in range(len(nums)):
            if len(stack) == 0:
                result[i] = -1
            elif nums[i] <= nums[stack[-1]]:
                result[i] = stack[-1]
            else:
                while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = -1
                else:
                    result[i] = stack[-1]
            stack.append(i)
        return result
    def nge():
        stack = []
        result = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if len(stack) == 0:
                result[i] = len(nums)
            elif nums[i] < stack[-1][0]:
                result[i] = stack[-1][1]
            else:
                while len(stack) != 0 and nums[i] >= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = len(nums)
                else:
                    result[i] = stack[-1][1]
            stack.append([nums[i],i])
        return result
    nums_pse = pse()
    nums_nse = nse()
    nums_pge = pge()
    nums_nge = nge()
    print(nums_pge,nums_pse)
    print(nums_nge,nums_nse)
    for i in range(len(nums)):
        temp = nums[i]
        if i == 0 or nums_pse[i] == -1:
            left = i + 1
        else:
            left = i - nums_pse[i] 
        right = nums_nse[i] - i  
        ans += (temp*left*right)
    sum_max = 0
    for i in range(len(nums)):
        temp = nums[i]
        if i == 0 or nums_pge[i] == -1:
            left = i + 1
        else:
            left = i - nums_pge[i] 
        right = nums_nge[i] - i  
        sum_max += (temp*left*right) 
        print(nums[i],left,right,sum_max)
    return sum_max - ans

nums = [71,55,82,55]
print(nums)
print(sumSubnumsayMins(nums))