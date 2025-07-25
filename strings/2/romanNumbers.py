def romanToInt(s):
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    ans = values[s[-1]]
    for i in range(len(s)-2,-1,-1):
        if values[s[i]] < values[s[i+1]]:
            ans -= values[s[i]]
        else:
            ans += values[s[i]]
    return ans

s = "MCMXCIV"
print(romanToInt(s))