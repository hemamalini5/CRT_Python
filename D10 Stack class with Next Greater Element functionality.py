# Stack class with Next Greater Element functionality
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

    def next_greater_elements(self):
        n = len(self.stack)
        result = [-1] * n  # Initialize result array with -1
        temp_stack = []    # Stack to store indices

        for i in range(n):
            # Pop elements from temp_stack smaller than current element
            while temp_stack and self.stack[i] > self.stack[temp_stack[-1]]:
                index = temp_stack.pop()
                result[index] = self.stack[i]
            temp_stack.append(i)

        return result

# Driver code
s = Stack()

# Read input integers (space-separated)
elements = list(map(int, input("Enter integer elements for the stack: ").split()))

# Push elements to stack
for elem in elements:
    s.push(elem)

# Find next greater elements
nge = s.next_greater_elements()

# Display results
print("Stack Elements:", s.stack)
print("Next Greater Elements on Right:", nge)
