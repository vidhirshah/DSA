def minimum(nums):
    min_val = float('inf')
    for num in nums:
        if num != 0:
            min_val = min(min_val, num)
    return min_val

def beautySum(s):
    sum = 0
    length = len(s)
    if length == 0 or length == 1 or length == 2:
        return 0
    for i in range(length):
        max_freq = 0
        min_freq = 0
        freq = [0]*26
        for j in range(i,length):
            letter = ord(s[j]) - ord('a')
            freq[letter] += 1
            max_freq = max(freq)
            min_freq = minimum(freq)
            if i != j and max_freq - min_freq > 0:
                sum += max_freq - min_freq
    return sum

s = "mwxjlbmbpyofvovaxwrddmzjqesdhkeriuittjahszpnspvkgsrgswnpch"
print(beautySum(s))

# nums = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(minimum(nums))