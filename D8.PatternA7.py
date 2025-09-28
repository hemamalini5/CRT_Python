'''
a b c
a b 
a
'''
n = 3   # number of rows

for i in range(n):
    for j in range(n - i):
        print(chr(97 + j), end=" ")
    print()
