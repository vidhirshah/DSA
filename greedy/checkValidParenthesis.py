def function(s,index,count):
    if count < 0 :
        return False
    if index < len(s):
        if s[index] == "(":
            return function(s,index+1,count+1)
        elif s[index] == ")":
            return function(s,index+1,count-1)
        elif s[index] == "*":
            return function(s,index+1,count) or function(s,index+1,count-1) or function(s,index+1,count+1)
    else:
        if count != 0:
            return False
        else:
            return True
    return True

def checkValidString(s):
    return function(s,0,0)
s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"


print(checkValidString(s))