'''
    A
  B B
C C C 
'''

n = 3   # number of rows

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    # Print the same letter (i+1) times
    char_to_print = chr(65 + i)   # 65 = 'A'
    for k in range(i + 1):
        print(char_to_print, end=" ")
    
    print()
