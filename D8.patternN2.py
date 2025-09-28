''' 4 3 2 1
    4 3 2 
    4 3 
    4'''
n = 4
for i in range(n):
    for j in range(n, i, -1):
        print(j, end=' ')
    print()