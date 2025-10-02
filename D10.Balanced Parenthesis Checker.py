# Balanced Parenthesis Checker

def is_balanced(expression):
    stack = []
    # Dictionary to map closing to opening brackets
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Driver code
expression = input("Enter the Expression: ")

if is_balanced(expression):
    print("User Entered Expression is a balanced parenthesis")
else:
    print("User Entered Expression is an inbalanced parenthesis")