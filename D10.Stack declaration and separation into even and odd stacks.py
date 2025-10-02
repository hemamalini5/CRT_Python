# Stack declaration and separation into even and odd stacks

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


# Driver code
original_stack = Stack()

# Read input integers (space-separated)
elements = list(map(int, input("Enter integer elements for the stack: ").split()))

# Push elements to original stack
for elem in elements:
    original_stack.push(elem)

print("Original Stack:")
original_stack.display()

# Separate even and odd numbers using filter
even_stack = Stack()
odd_stack = Stack()

even_numbers = list(filter(lambda x: x % 2 == 0, original_stack.stack))
odd_numbers = list(filter(lambda x: x % 2 != 0, original_stack.stack))

for num in even_numbers:
    even_stack.push(num)

for num in odd_numbers:
    odd_stack.push(num)

print("Even Stack:")
even_stack.display()

print("Odd Stack:")
odd_stack.display()