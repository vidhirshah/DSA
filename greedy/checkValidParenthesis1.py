def function(s,index,count):
    minimum = 0
    maximum = 0
    count = 0
    for i in s:
        if i == "(":
            minimum += 1
            maximum += 1
        elif i == ")":
            minimum -= 1
            maximum -= 1
        elif i == "*":
            minimum -= 1
            maximum += 1
        if minimum < 0:
            minimum = 0
        if minimum < 0:
            return False
        if maximum < 0:
            return False
    if minimum == 0:
        return True
    return False

def checkValidString(s):
    return function(s,0,0)
s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"


print(checkValidString(s))