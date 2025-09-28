#read the 5 elements as input from the user and print the square values of list elements without loops
# Read and convert the input numbers, same as the first step
numbers = list(map(int, input("Enter 5 numbers separated by spaces: ").split()))

# Use map() to apply a lambda function (x**2) to each number in the list
squares = list(map(lambda x: x**2, numbers))

# Print the resulting list of squares
print(squares)


