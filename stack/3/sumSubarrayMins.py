def sumSubarrayMins(arr: list[int]) -> int:
    ans = 0
    def pse():
        stack = []
        result = [0]*len(arr)
        for i in range(len(arr)):
            if len(stack) == 0:
                result[i] = -1
            elif arr[i] >= arr[stack[-1]]:
                result[i] = stack[-1]
            else:
                while len(stack) != 0 and arr[i] < arr[stack[-1]]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = -1
                else:
                    result[i] = stack[-1]
            stack.append(i)
        return result
    def nse():
        stack = []
        result = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            if len(stack) == 0:
                result[i] = len(arr)
            elif arr[i] > stack[-1][0]:
                result[i] = stack[-1][1]
            else:
                while len(stack) != 0 and arr[i] <= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    result[i] = len(arr)
                else:
                    result[i] = stack[-1][1]
            stack.append([arr[i],i])
        return result
    arr_pse = pse()
    arr_nse = nse()
    # print(arr_pse)
    # print(arr_nse)
    for i in range(len(arr)):
        temp = arr[i]
        if i == 0 or arr_pse[i] == -1:
            left = i + 1
        else:
            left = i - arr_pse[i] 
        right = arr_nse[i] - i  
        ans += (temp*left*right) % (10**9+7)
        # print(arr[i],left,right,ans)
    return ans

arr = [71,55,82,55]
print(arr)
print(sumSubarrayMins(arr))