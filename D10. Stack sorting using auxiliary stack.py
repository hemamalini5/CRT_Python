# Stack sorting using auxiliary stack

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


def sort_stack(input_stack):
    aux_stack = Stack()

    while not input_stack.is_empty():
        # Pop the top element from input stack
        temp = input_stack.pop()

        # Move elements from aux_stack back to input_stack if they are greater than temp
        while not aux_stack.is_empty() and aux_stack.peek() > temp:
            input_stack.push(aux_stack.pop())

        # Push temp in the correct position in aux_stack
        aux_stack.push(temp)

    return aux_stack


# Driver code
s = Stack()

# Read input integers (space-separated)
elements = list(map(int, input("Enter integer elements for the stack: ").split()))

# Push elements to stack
for elem in elements:
    s.push(elem)

print("Original Stack:")
s.display()

# Sort the stack
sorted_stack = sort_stack(s)

print("Sorted Stack (Ascending Order):")
sorted_stack.display()