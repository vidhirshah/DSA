def lengthOfLIS(nums:list):
    result = []
    def bs(number):
        left = 0
        right = len(result) -1 
        while left <= right:
            mid = int((left+right)/2)
            if result[mid] == number:
                return mid
            elif result[mid] < number:
                left = mid + 1
            else:
                right = mid - 1
        return left
    for i in nums:
        if len(result) == 0:
            result.append(i)
        elif result[-1] < i:
            result.append(i)
        else:
            index = bs(i)
            result[index] = i
        print(i,result)
    return len(result)

nums = [3,5,6,2,5,4,19,5,6,7,12]
print(lengthOfLIS(nums))