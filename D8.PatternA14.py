'''
    a
  b b 
c c c
'''

n = 3   # number of rows

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    # Print same letter (i+1) times
    char_to_print = chr(97 + i)  # 'a' for row 0, 'b' for row 1, 'c' for row 2
    for k in range(i + 1):
        print(char_to_print, end=" ")

    print()
