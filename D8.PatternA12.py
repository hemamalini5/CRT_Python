'''
A B C 
A B 
A
'''

n = 3   # number of rows

for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()
