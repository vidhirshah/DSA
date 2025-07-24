def hash(s:str):
    temp_hash = [0]*26
    for i in range(len(s)):
        temp_hash[ord(s[i]) - ord('a')] = temp_hash[ord(s[i]) - ord('a')] + 1
    return temp_hash

print(hash("aswfcvgyxwducbnhouwefcnhasdjiiiiweryhbgcdnasiyufbhcuyoiwynciwuscdyqawondqryuawmjiowqqeoibcsdhiancvayyycvbhaovfileepwrtnvjw"))