'''
  a
 a b
a b c
'''
n = 3  # height of pyramid

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print letters
    for k in range(i):
        print(chr(97 + k), end=" ")
    
    # Move to next line
    print()
