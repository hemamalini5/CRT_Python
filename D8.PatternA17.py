'''
a b c d
  a b c
    a b
      a
'''
n = 4   # number of rows

for i in range(n):
    # Print leading spaces
    for j in range(i):
        print("  ", end=" ")  # 2 spaces for alignment

    # Print letters
    for k in range(n - i):
        print(chr(97 + k), end=" ")

    print()
