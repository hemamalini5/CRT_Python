'''
a
b b 
c c c
'''
n=3
for i in range(n):
    for j in range(i+1):
        print(chr(97+i),end=" ")
    print()