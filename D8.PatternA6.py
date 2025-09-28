'''
C C C
B B
A
'''
n=3
for i in range(n):
    char_to_print = chr(65 + (n - 1 - i))
    for j in range(n - i):
        print(char_to_print, end=" ")
    print()