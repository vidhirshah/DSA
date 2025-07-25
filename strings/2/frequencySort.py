from collections import Counter

def frequencySort(s):
    freq = Counter(s)
    freq = sorted(freq.items(), key = lambda x : -x[1])
    result = ""
    for char,i in freq:
        result = result + char*(i)
    return result

s = "cccaaa"
print(frequencySort(s))