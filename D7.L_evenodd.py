#read a list of numbers and print the list of even or odd numbers without using loops& conditional statements
# Read input and convert to a list of integers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Filter the even numbers using a lambda and the filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Filter the odd numbers using a lambda and the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
