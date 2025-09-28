'''
D D D D
  C C C
    B B
      A
  '''
n = 4   # number of rows

for i in range(n):
    # Print leading spaces
    for j in range(i):
        print("  ", end=" ")  # 2 spaces per indentation

    # Print repeated letters
    char_to_print = chr(65 + n - 1 - i)  # D, C, B, A
    for k in range(n - i):
        print(char_to_print, end=" ")

    print()
