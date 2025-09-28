'''
    a
  a b
a b c
'''

n = 3   # number of rows

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    # Print increasing letters
    for k in range(i + 1):
        print(chr(97 + k), end=" ")
    
    print()
