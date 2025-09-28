'''
- - A
- A B
A B C
'''
n = 3   # number of rows

for i in range(n):
    # Print dashes
    for j in range(n - i - 1):
        print("-", end=" ")

    # Print letters
    for k in range(i + 1):
        print(chr(65 + k), end=" ")
    
    print()
