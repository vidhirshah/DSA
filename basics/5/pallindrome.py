def check_pallindrome(inp:str,index:int):
    print(index)
    if index == int(len(inp)/2):
        if inp[index] == inp[len(inp) - 1 - index]:
            return True
        return False
    if inp[index] != inp[len(inp) - 1 - index]:
        return False
    return True and check_pallindrome(inp, index + 1)

def isPalindrome(s:str):
    s = s.lower()
    processed = ""
    for i in s:
        if i.isalnum():
            processed = processed + i
    if len(processed) < 1:
        return True
    return check_pallindrome(processed,0)

print(isPalindrome(""))