def swap(a,b):
    print(a,b)
    a = a ^ b
    b = b ^ a
    a = b ^ a
    return a,b

a = 234
b = 100
print(swap(a,b))
