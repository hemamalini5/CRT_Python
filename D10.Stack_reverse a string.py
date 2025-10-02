# Reverse a string using stack

# Function to reverse string
def reverse_string(input_str):
    stack = []  # Initialize stack
    
    # Push all characters onto stack
    for char in input_str:
        stack.append(char)
    
    # Pop characters from stack to reverse
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Read input
original_str = input("Enter a string: ")

# Reverse using stack
reversed_str = reverse_string(original_str)

print("Reversed String:", reversed_str)
