def letterCombinations(digits):
    if digits == "":
        return []
    dig_to_letters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    result = []
    def helper(ans,i):
        if i == len(digits):
            result.append(ans)
            return
        for s in dig_to_letters[digits[i]]:
            helper(ans+s,i+1)
        return
    helper("",0)
    return result

nums = "2"
print(letterCombinations(nums))