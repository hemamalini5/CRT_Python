'''
d d d d
  c c c
    b b
      a
'''

n = 4   # number of rows

for i in range(n):
    # Print leading spaces
    for j in range(i):
        print("  ", end=" ")  # 2 spaces for alignment

    # Print repeated letters
    char_to_print = chr(97 + n - 1 - i)  # d, c, b, a
    for k in range(n - i):
        print(char_to_print, end=" ")

    print()
